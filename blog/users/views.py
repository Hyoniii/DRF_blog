import json

import bcrypt
from django.http import JsonResponse
from rest_framework import generics, permissions, viewsets

from users.serializers import UserSerializer

from .models import User

# Create your views here.

class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    print(queryset,"!!")
    print(serializer_class,"@@")
    print("--------")
    
    def post(self,request):
        try:
            data         = json.loads(request.body)
            password     = data['password']
            re_password  = data['re_password']
            if User.objects.filter(email = data['email']).exists():
                return JsonResponse({'message':'Existing user'},status=409)
            print(data)
            print('~~~~')
            print(password)
            print(re_password)
            return JsonResponse({'message':'SUCCESS'},status=201)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
    
