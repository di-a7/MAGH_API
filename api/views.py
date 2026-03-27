from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, OrderItem
from .serializer import CategorySerializer
# Create your views here.

@api_view(['GET','POST'])
def categorylist(request):
   if request.method == 'GET':
      category = Category.objects.all()
      serializer = CategorySerializer(category, many = True)        # serialize : python objects convert to json
      return Response(serializer.data)
   
   elif request.method == "POST":
      serializer = CategorySerializer(data = request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data)

@api_view(['GET','DELETE'])
def categoryDetail(request, id):
   category = Category.objects.get(id = id)
   if request.method == 'GET':
      serializer = CategorySerializer(category)        # serialize : python objects convert to json
      return Response(serializer.data)
   
   elif request.method == 'DELETE':
      items = OrderItem.objects.filter(food__category = category).count()
      if items > 0:
         return Response({"detail":"Protected Error: Category can't be deleted. Related to OrderItem"})
      category.delete()
      return Response({"detail":"Data has be deleted."})

# tablelist 