from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('category',CategoryModelViewset, basename = 'category')
router.register('foods',FoodModelViewset)
# router.register('category/<id>/',CategoryDetailViewset, basename = 'category_detail')

urlpatterns = [
   # path('category/',CategoryViewset.as_view({'get':'list','post':'create'})),
   # path('category/<id>/', CategoryDetailViewset.as_view({'get':'retrieve','put':'update','delete':'destroy'}))
] + router.urls
