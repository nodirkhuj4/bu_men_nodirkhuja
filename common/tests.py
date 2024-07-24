import tempfile
from rest_framework.test import APITestCase

from common import models, serializers

class TestSettings(APITestCase):

    def test_api_settings_list(self):
        settings_data = {
            "email": "a@a.com",
            "links": "https://github.com/",
            "contact_phone": "+998978824042",
            "longitude": 1000,
            "latitude": 2000,
            "location_text": "Toshkent-chilonzor"
        }
        setting = models.Settings.objects.create(**settings_data)

        serializer = serializers.SettingSerializer(setting)

        response = self.client.get("/api/v1/common/settings")

        assert response.status_code == 200
        assert serializer.data == settings_data
        

class TestNews(APITestCase):

    def test_api_news_listing(self):
        news_data1 = {
            "title": "a@a.com",
            "content": "<p>fasdfjakdjf</p>",
            "slug": "toshkent-chilonzor"
        }

        news_data2 = {
            "title": "a.com",
            "content": "<p>fasdfjakdjf1</p>",
            "slug": "toshkent-chilonzor1"
        }


        news = models.News.objects.create(**news_data1)
        news2 = models.News.objects.create(**news_data2)

        serializer = serializers.NewSerializer(news)

        response = self.client.get("/api/v1/common/list/news")

        assert response.status_code == 200
        assert serializer.data == news_data1
        assert len(response.data) == 2

    def test_api_news_detail(self):
        
        news_data1 = {
            "title": "a@a.com",
            "content": "<p>fasdfjakdjf</p>",
            "slug": "toshkent-chilonzor"
        }

        news_data2 = {
            "title": "a.com",
            "content": "<p>fasdfjakdjf1</p>",
            "slug": "toshkent-chilonzor1"
        }


        news = models.News.objects.create(**news_data1)
        news2 = models.News.objects.create(**news_data2)

        serializer = serializers.NewSerializer(news2)

        response = self.client.get("/api/v1/common/news/toshkent-chilonzor1")

        assert response.status_code == 200
        assert response.data == serializer.data


class TestQuotes(APITestCase):

    def test_api_show_quotes(self):


        quotes1 = {
            "author": "a@a.com",
            "content": "<p>fasdfjakdjf</p>",
        }

        quotes2 = {
            "author": "a.com",
            "content": "<p>fasdfjakdjf1</p>",
        }


        quotes1 = models.Quotes.objects.create(**quotes1)
        quotes2 = models.Quotes.objects.create(**quotes2)

        serializer = serializers.QuoteSerializer(quotes1)

        response = self.client.get("/api/v1/common/quotes")

        assert response.status_code == 200
        assert serializer.data == response.data[0]
        assert len(response.data) == 2


class TestFAQ(APITestCase):

    def test_api_listing_faq(self):


        faq_data1 = {
            "question": "What is your name?",
            "answer": "My name is nodirkhuja"
        }

        faq_data2 = {
            "question": "How old are you?",
            "answer": "I am 23 years old"
        }

        faq1 = models.FAQ.objects.create(**faq_data1)
        faq2 = models.FAQ.objects.create(**faq_data2)

        serializer = serializers.FAQSerializer(faq1)

        response = self.client.get("/api/v1/common/faq")

        assert response.status_code == 200
        assert serializer.data == response.data[0]
        assert len(response.data) == 2


class TestADS(APITestCase):

    def test_api_ads_show(self):

        image1 = tempfile.NamedTemporaryFile(suffix='.jpg').name
        image2 = tempfile.NamedTemporaryFile(suffix='.jpg').name
        image3 = tempfile.NamedTemporaryFile(suffix='.jpg').name
    

        expected_data = [image1, image2, image3]


        image1 = models.Advertising.objects.create(image=image1)
        image2 = models.Advertising.objects.create(image=image2)
        image3 = models.Advertising.objects.create(image=image3)

        serializer = serializers.AdvertisingSerializer(image1)

        response = self.client.get("/api/v1/common/ads")
        print(response.data)

        assert response.status_code == 200
        assert response.data == expected_data
        assert len(response.data) == 3 
       