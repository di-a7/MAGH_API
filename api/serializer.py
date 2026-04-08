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

class OrderItemSerializer(serializers.ModelSerializer):
   food = serializers.StringRelatedField()
   food_id = serializers.PrimaryKeyRelatedField(queryset = Food.objects.all())
   class Meta:
      model = OrderItem
      fields = ['food_id','food']

class OrderSerializer(serializers.ModelSerializer):
   user = serializers.HiddenField(default = serializers.CurrentUserDefault())
   items = OrderItemSerializer(many=True)
   status = serializers.CharField(read_only=True)
   total_price = serializers.IntegerField(read_only=True)
   class Meta:
      model = Order
      fields = ['id','user','total_price','status','items']
   
   def create(self, validated_data):
      items = validated_data.pop('items')
      total = 0
      for i in items:
         food = Food.objects.get(id = i.get('food_id').id)
         total += food.price
      order = Order.objects.create(user = validated_data.get('user'), total_price = total)
      
      for i in items:
         OrderItem.objects.create(order = order, food = i.get('food_id'))
      
      return order

# items = [
#    {
#    "food": 16
#    },
# {
#    "food": 17
#    }
# ]
# }


# class CategorySerializer(serializers.Serializer):
#    id = serializers.IntegerField(read_only=True)
#    name = serializers.CharField()
   
#    def create(self, validated_data):
#       category = Category.objects.create(name = validated_data.get('name'))
#       return category
   
   # validated_data = {"name":"new data"}