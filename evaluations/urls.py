from django.urls import path, include
from rest_framework import routers

from . import views

app_name = 'courses'

router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet, basename='course_list')
router.register('students', views.CourseStudentViewSet, basename='course_student')
# router.register('mycourses', views.MyCoursesStudentViewSet, basename='mycourse_student')

urlpatterns = [
# CRUD COURSES
  path('', include(router.urls)),
  path('course/create/', views.CourseCreateAPIView.as_view(), name='create_course'),
  path('course/update/<int:pk>/', views.CourseUpdateAPIView.as_view(), name='update_course'),
  path('course/delete/<int:pk>/', views.CourseDeleteAPIView.as_view(), name='delete_course'),
  path('notes/create/', views.NotesCreateAPIView.as_view(), name='create_notes'),
  path('mycourses/<int:pk>/', views.MyCoursesStudentViewSet.as_view(), name='mycourses'),

]
