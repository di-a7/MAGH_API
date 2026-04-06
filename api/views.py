from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import CategorySerializer, FoodSerializer
from rest_framework import status
# Create your views here.

# ModelViewset
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
# from rest_framework.pagination import PageNumberPagination
# from .pagination import FoodPagiation, CategoryPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .filters import FoodFilter
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthenticatedOrReadOnly
class CategoryModelViewset(ModelViewSet):
   queryset = Category.objects.all()
   serializer_class = CategorySerializer
   # pagination_class = CategoryPagination
   filter_backends = [DjangoFilterBackend]
   permission_classes = [IsAuthenticated]
   filterset_fields = ['name']
   
   
   def destroy(self, request,pk):
      category = Category.objects.get(pk = pk)
      items = OrderItem.objects.filter(food__category = category).count()
      if items > 0:
         return Response({"detail":"Protected Error: Category can't be deleted. Related to OrderItem"})
      category.delete()
      return Response({"detail":"Data has be deleted."})

class FoodModelViewset(ModelViewSet):
   queryset = Food.objects.all().select_related('category')
   serializer_class = FoodSerializer
   # pagination_class = FoodPagiation
   filter_backends = [filters.SearchFilter, DjangoFilterBackend]
   search_fields = ['name']
   permission_classes = [IsAuthenticatedOrReadOnly]
   # filterset_fields = ['category']
   filterset_class = FoodFilter

# Viewset
# from rest_framework.viewsets import ViewSet
# class CategoryViewset(ViewSet):
#    def list(self, request):
#       category = Category.objects.all()
#       serializer = CategorySerializer(category, many = True)        # serialize : python objects convert to json
#       return Response(serializer.data)
   
#    def create(self, request):
#       serializer = CategorySerializer(data = request.data)
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)

# class CategoryDetailViewset(ViewSet):
#    def retrieve(self, request, id):
#       category = Category.objects.get(id = id)
#       serializer = CategorySerializer(category)        # serialize : python objects convert to json
#       return Response(serializer.data)
   
#    def update(self,request,id):
#       category = Category.objects.get(id = id)
#       serializer = CategorySerializer(category,data = request.data)
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response(serializer.data)
   
#    def destroy(self, request,id):
#       category = Category.objects.get(id = id)
#       items = OrderItem.objects.filter(food__category = category).count()
#       if items > 0:
#          return Response({"detail":"Protected Error: Category can't be deleted. Related to OrderItem"})
#       category.delete()
#       return Response({"detail":"Data has be deleted."})



# from rest_framework import generics
# class CategoryList(generics.ListCreateAPIView):
#    queryset = Category.objects.all()
#    serializer_class = CategorySerializer

# class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
#    queryset = Category.objects.all()
#    serializer_class = CategorySerializer
#    lookup_field = 'id'
   
#    def delete(self,request,id):
#       category = Category.objects.get(id = id)
#       items = OrderItem.objects.filter(food__category = category).count()
#       if items > 0:
#          return Response({"detail":"Protected Error: Category can't be deleted. Related to OrderItem"})
#       category.delete()
#       return Response({"detail":"Data has be deleted."})



# Mixins
# from rest_framework import mixins

# class CategoryGeneric(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#    queryset = Category.objects.all()
#    serializer_class = CategorySerializer
   
#    def get(self, request):
#       return self.list(self,request)
   
#    def post(self,request):
#       return self.create(self,request)




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