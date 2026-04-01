from rest_framework import serializers
from .models import *
class CategorySerializer(serializers.ModelSerializer):
   class Meta:
      model = Category
      fields = '__all__'
      # fields = ['id','name']
      # exclude = ['name']


class FoodSerializer(serializers.ModelSerializer):
   category_id = serializers.PrimaryKeyRelatedField(queryset = Category.objects.all())
   category = serializers.StringRelatedField()
   price_with_vat = serializers.SerializerMethodField()
   class Meta:
      model = Food 
      fields = ["id","name","price","price_with_vat","category_id","category"]
   
   def get_price_with_vat(self, food:Food):
      return food.price + food.price * 0.12
   
   # with 10% discount, method, field, fields include


# class CategorySerializer(serializers.Serializer):
#    id = serializers.IntegerField(read_only=True)
#    name = serializers.CharField()
   
#    def create(self, validated_data):
#       category = Category.objects.create(name = validated_data.get('name'))
#       return category
   
   # validated_data = {"name":"new data"}