from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
# Create your views here.
class LoginView(APIView):
   def post(self,request):
      username = request.data.get("username")
      password = request.data.get("password")
      if username == '' or password == '':
         return Response({"detail":"both username and password are required."})
      user = authenticate(username = username, password = password)       # User.objects.filter(username=useranme, password=password)
      if user:
         token,_ = Token.objects.get_or_create(user=user)
         return Response({"username":f"{username}", "token": token.key})
      return Response({"detail":"Invalid Credentials"})
