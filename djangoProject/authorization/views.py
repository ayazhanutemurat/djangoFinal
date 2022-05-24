from django.shortcuts import render
import json

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, status, generics
# Create your views here.
from authorization.models import User
from authorization.serializer import RegistrationSerializer
class RegisterView(APIView):
    def post(self, request):
        try:
            if User.objects.filter(username=request.data.get('username')).first():
                raise Exception('Not found')
            serializer = RegistrationSerializer(data={"username": request.data.get('username'),
                                                      "password": request.data.get('password'),
                                                      "email": request.data.get('email'),
                                                      "first_name": request.data.get('first_name'),
                                                      "last_name": request.data.get('last_name')})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)