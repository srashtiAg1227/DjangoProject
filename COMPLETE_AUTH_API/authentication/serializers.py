from rest_framework import serializers
from .models import MyUser

class UserRegistrationSerializer(serializers.ModelSerializer):
   password2 = serializers.CharField(style= {'input_type':'password'}, write_only = True) 
   class Meta:
      model = MyUser
      fields =['email','name','password','password2']
      extra_kwargs = {
         'password' :{'write_only': True}
      }

   def validate(self, data):
         password = data.get('password')
         password2 = data.get('password2')
         
         if (password != password2):
            raise serializers.ValidationError('Confirm Password does not match Password !!')
         return data
      
   def create(self, validate_data):
         print("creating")
         return MyUser.objects.create_user(**validate_data)
   

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = MyUser
        fields =['email', 'password']

class PasswordEncryptionSerializer(serializers.Serializer):
    password = serializers.CharField()
