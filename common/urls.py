from common import views

from django.urls import path

urlpatterns=[
    path('settings', views.SettingsView.as_view(), name='common-settings'),
    path('list/news', views.NewsListView.as_view(), name='common-news-list'),
    path('user/application',views.CreateContactApplication.as_view(), name='common-user-application-create'),
    path('news/<str:slug>', views.NewsDetailView.as_view(), name='common-news-detail'),
    path('quotes', views.QuotesView.as_view(), name='common-quotes'),
    path('ads', views.AdvertisingView.as_view(), name='common-ads'),
    path('faq', views.FAQView.as_view(), name='common-faq'),

]