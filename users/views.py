from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser

from users.serializers import (
    UserSerializer,
    UserProfileSerializer
)

from users.models import (
    Profile
)

from django.contrib.auth.models import User

from django.forms.models import model_to_dict


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        user_serializer = UserProfileSerializer(user)
        token['user'] = user_serializer.data
        return token

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = User.objects.filter(profile__tipo=3)
    permission_classes = (IsAuthenticated, )


class UserCreateAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class UserUpdateAPIView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated, )

    def update(self, request, *args, **kwargs):
        user = User.objects.get(pk=self.kwargs['pk'])
        print(getattr(User.profile, 'user_profile', []))
        
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            users = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class UserDeleteAPIView(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated, )

    def delete(self, request, *args, **kwargs):
        try:
            user = User.objects.get(pk=self.kwargs['pk'])
            user.delete()
            return Response(status = status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response(status = status.HTTP_400_BAD_REQUEST)