from django.shortcuts import render
from .serializers import * 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            msg = {
                'message':'Registration Successful'
            }
            return Response(msg, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
