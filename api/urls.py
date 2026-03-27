from django.urls import path, include
from .views import categorylist, categoryDetail
urlpatterns = [
   path('category/',categorylist),
   path('category/<id>/', categoryDetail)
]
