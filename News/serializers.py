from rest_framework import serializers
from .models import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io


# class ProductModel:
#     def __init__(self, prod_name, description):
#         self.prod_name = prod_name
#         self.description = description

class NewsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsType
        fields = ("name", "color")



class NewsReadSerializer(serializers.ModelSerializer):
    news_type = NewsTypeSerializer()
    class Meta:
        model = News
        fields = ("title", "description", "full_description", "news_type")
        # fields = ("__all__")

class NewsWriteSerializer(serializers.ModelSerializer):
    # news_type = NewsTypeSerializer()
    class Meta:
        model = News
        fields = ("title", "description", "full_description", "news_type")
        # fields = ("__all__")
