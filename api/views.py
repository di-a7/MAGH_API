from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, OrderItem
from .serializer import CategorySerializer
from rest_framework import status
# Create your views here.
# Mixins
from rest_framework import mixins
from rest_framework.generics import GenericAPIView

class CategoryGeneric(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
   queryset = Category.objects.all()
   serializer_class = CategorySerializer
   
   def get(self, request):
      return self.list(self,request)
   
   def post(self,request):
      return self.create(self,request)




# Class based(APIView)
# from rest_framework.views import APIView

# class CategoryList(APIView):
#    def get(self, request):
#       category = Category.objects.all()
#       serializer = CategorySerializer(category, many = True)        # serialize : python objects convert to json
#       return Response(serializer.data)
   
#    def post(self, request):
#       serializer = CategorySerializer(data = request.data)
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)


# class CategoryDetail(APIView):
#    def get(self,request, id):
#       category = Category.objects.get(id = id)
#       serializer = CategorySerializer(category)        # serialize : python objects convert to json
#       return Response(serializer.data)
   
#    def put(self,request,id):
#       category = Category.objects.get(id = id)
#       serializer = CategorySerializer(category, data = request.data)
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response(serializer.data)
   
#    def patch(self,request,id):
#       category = Category.objects.get(id = id)
#       serializer = CategorySerializer(category, data = request.data, patial = True)
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response(serializer.data)
   
#    def delete(self,request,id):
#       category = Category.objects.get(id = id)
#       items = OrderItem.objects.filter(food__category = category).count()
#       if items > 0:
#          return Response({"detail":"Protected Error: Category can't be deleted. Related to OrderItem"})
#       category.delete()
#       return Response({"detail":"Data has be deleted."})
















# Function based (api_view)

# @api_view(['GET','POST'])
# def categorylist(request):
#    if request.method == 'GET':
#       category = Category.objects.all()
#       serializer = CategorySerializer(category, many = True)        # serialize : python objects convert to json
#       return Response(serializer.data)
   
#    elif request.method == "POST":
#       serializer = CategorySerializer(data = request.data)
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response(serializer.data)

# @api_view(['GET','DELETE'])
# def categoryDetail(request, id):
#    category = Category.objects.get(id = id)
#    if request.method == 'GET':
#       serializer = CategorySerializer(category)        # serialize : python objects convert to json
#       return Response(serializer.data)
   
#    elif request.method == 'DELETE':
#       items = OrderItem.objects.filter(food__category = category).count()
#       if items > 0:
#          return Response({"detail":"Protected Error: Category can't be deleted. Related to OrderItem"})
#       category.delete()
#       return Response({"detail":"Data has be deleted."})

# CRUD operation
# tablelist :
# tabledetail :