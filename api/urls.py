from django.urls import path, include
from .views import *
urlpatterns = [
   path('category/',CategoryGeneric.as_view()),
   # path('category/<id>/', CategoryDetail.as_view())
]
