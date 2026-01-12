from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import *

# Create your views here.


class RegisterView(APIView):
    permission_classes=[AllowAny] #कोणीही register करू शकतो
    
    def post(self,request):
        serializer=RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True) #Data valid check
        serializer.save()
        return Response(
            {
                "msg":"User register success."
            }
        )    
    
    