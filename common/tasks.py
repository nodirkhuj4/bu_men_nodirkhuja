from datetime import timedelta
from celery import shared_task

from common.models import NewsView, News

from django.utils import timezone
from django.db.models import F

@shared_task
def add_news_view(news, visitor_id, ip):
    count = NewsView.objects.filter(news=news, 
                                    created_at=timezone.now() - timedelta(hours=1),
                                    ip=ip).count()
    
    
    if count >= 1000:
        print(f"{ip} oxirgi soat ichida 1000 tadan ko'p ko'rish yaratgan")
        return
        
    if NewsView.objects.filter(news=news, visitor=visitor_id).exists():
        print(f"{news}: {visitor_id} bu yangilikni aval ko'rgan") 
        return
    
    NewsView.objects.create(
        news_id=news, 
        visitor=visitor_id, 
        ip=ip
        )

    News.objects.filter(pk=news).update(
        view_count=F('view_count') + 1
        )
    

