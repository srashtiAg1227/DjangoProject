from django.shortcuts import render
from .serializers import * 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password

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


class UserLoginView(APIView):

    def get_tokens_for_user(self,user):
        refresh = RefreshToken.for_user(user)

        return {
         'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

    def post(self, request):
        serializer = UserLoginSerializer(data= request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user =MyUser.objects.get(email = email)
            if user is not None:
                if(user.password ==password):
                     token = self.get_tokens_for_user(user)
                     msg = {
                    'token' : token,
                    'message':'login Successful'
                   }
                     return Response(msg, status= status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordEncryptionView(APIView):
    def post(self, request):
        serializer = PasswordEncryptionSerializer(data= request.data)
        if serializer.is_valid():
            password =  serializer.validated_data['password']
            # i have used the same salt value for encryption while storing password in db 
            # explicitly specified salt in set_password method of python's default AbstractBaseUser class
            encrypted_password = make_password(password, salt='D;%yL9TS:5PalS/d')
            return Response({'encrypted_password': encrypted_password}, status= status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)