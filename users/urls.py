from django.urls import path, include
from rest_framework import routers

from . import views

app_name = 'users'

router = routers.DefaultRouter()
router.register('users', views.UserViewSet, basename='users_list')

urlpatterns = [
  path('token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
# CRUD USERS
  path('', include(router.urls)),
  path('users/create/', views.UserCreateAPIView.as_view(), name='create_user'),
  path('users/update/<int:pk>/', views.UserUpdateAPIView.as_view(), name='update_users'),
  path('users/delete/<int:pk>/', views.UserDeleteAPIView.as_view(), name='delete_users'),
]