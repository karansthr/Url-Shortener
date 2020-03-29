import re

from django.core.validators import URLValidator
from rest_framework import serializers

from shortener import models, utils


class UrlCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.URL
        fields = ['link', 'custom_short_link', 'shortened']

    link = serializers.CharField()
    custom_short_link = serializers.CharField(
        min_length=3, max_length=10, required=False)

    def create(self, validated_data):
        custom_short_link = None
        if 'custom_short_link' in validated_data:
            custom_short_link = validated_data['custom_short_link']
        validated_data['shortened'] = utils.encode(custom_short_link)
        if custom_short_link:
            validated_data.pop('custom_short_link')
        instance = models.URL.objects.create(**validated_data)
        return instance

    @staticmethod
    def validate_link(link):
        if link is None:
            raise serializers.ValidationError("Please enter a valid URL")
        link = 'http://' + link if link[:4] != 'http' else link

        try:
            val = URLValidator()
            val(link)
        except serializers.ValidationError:
            raise serializers.ValidationError("Please enter a valid URL")

        return link

    @staticmethod
    def validate_suggestion(custom_short_link):
        if custom_short_link:
            if custom_short_link in [
                    'about', 'disclaimer', 'contact', 'sitemap.xml',
                    'robots.txt', 'login', 'register', 'sitemap', 'doc',
                    'admin', 'karan', 'resume', 'profile', 'logout'
            ]:
                raise serializers.ValidationError(
                    'Please choose another custom short link, ' + custom_short_link +
                    ' is reserverd.')

            if not re.match("^[A-Za-z0-9_-]*$", custom_short_link):
                raise serializers.ValidationError(
                    " It should contain only alpha-numeric and/or _ ")

            if models.URL.objects.filter(shortened=custom_short_link).exists():
                raise serializers.ValidationError(
                    "Please choose another, '" + custom_short_link +
                    "' already exists.")

        return custom_short_link
