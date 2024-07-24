from common import models

from rest_framework import serializers

class SettingSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.Settings
        fields=[
            "email",
            "links",
            "contact_phone",
            "longitude",
            "latitude",
            "location_text"
        ]

class NewSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.News
        fields=[
            "title",
            "content",
            "slug",
        
        ]

class QuoteSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.Quotes
        fields=[
            "author",
            "content"
        ]

class AdvertisingSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.Advertising
        fields=["image"]


class FAQSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.FAQ
        fields=[
            "question",
            "answer"
        ]

class UserCreateApplication(serializers.ModelSerializer):

    class Meta:
        model=models.UserContactApplication
        fields=[
            "full_name",
            "phone",
            "message"
        ]