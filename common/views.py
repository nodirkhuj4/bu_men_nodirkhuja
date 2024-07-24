from common import models, serializers
from common.filters import NewsFilter
from common.throating import CreateContactApplicationPhoneNumberThrottle, CreateContactApplicationIPThrottle
from common.utility import get_client_ip
from common.tasks import add_news_view

from rest_framework.generics import (
                                    GenericAPIView, 
                                    ListAPIView,
                                    RetrieveAPIView,
                                    CreateAPIView,
                                    )
from rest_framework.response import Response

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters.rest_framework.backends import DjangoFilterBackend


class SettingsView(GenericAPIView):
    queryset = models.Settings.objects.all()
    serializer_class = serializers.SettingSerializer

    @method_decorator(cache_page(5*50))
    def get(self, request):
        setting = self.get_queryset().first()
        serializer = self.serializer_class(setting)
        return Response(serializer.data)


class NewsListView(ListAPIView):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilter 


class NewsDetailView(RetrieveAPIView):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewSerializer
    lookup_field = "slug"

    def get_object(self):
        news = super().get_object()
        news_id = news.id   
        visitor_id = self.request.META.get('HTTP_X_VISITOR_ID')
        ip = get_client_ip(self.request)
        
        if visitor_id:
            add_news_view.delay(news_id, visitor_id, ip)

        return news

class QuotesView(ListAPIView):
    queryset = models.Quotes.objects.all()
    serializer_class = serializers.QuoteSerializer


class AdvertisingView(ListAPIView):
    queryset = models.Advertising.objects.order_by('?')
    serializer_class = serializers.AdvertisingSerializer


class FAQView(ListAPIView):
    queryset = models.FAQ.objects.all()
    serializer_class = serializers.FAQSerializer

class CreateContactApplication(CreateAPIView):

    queryset = models.UserContactApplication.objects.all()
    serializer_class = serializers.UserCreateApplication
    throttle_classes = [CreateContactApplicationIPThrottle, CreateContactApplicationPhoneNumberThrottle]