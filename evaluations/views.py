from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser

from users.serializers import (
    UserSerializer,
)

from evaluations.serializers import (
    GradeSerializer, 
    CourseSerializer,
    NotesSerializer,
    CourseTeacherSerializer,
    CourseStudentSerializer,
    InfoStudentSerializer
)

from evaluations.models import (
    Course,
    Notes
)

from django.contrib.auth.models import User



class CourseViewSet(ModelViewSet):
    serializer_class = CourseTeacherSerializer
    queryset = Course.objects.all()
    permission_classes = (IsAuthenticated, )


class CourseCreateAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            course = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class CourseUpdateAPIView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated, )

    def update(self, request, *args, **kwargs):
        course = Course.objects.get(pk=self.kwargs['pk'])
        print(course)
        data = JSONParser().parse(request)
        serializer = CourseSerializer(course, data=data)
        if serializer.is_valid():
            courses = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class CourseDeleteAPIView(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated, )

    def delete(self, request, *args, **kwargs):
        try:
            course = Course.objects.get(pk=self.kwargs['pk'])
            course.delete()
            return Response(status = status.HTTP_201_CREATED)
        except Course.DoesNotExist:
            return Response(status = status.HTTP_400_BAD_REQUEST)


class CourseStudentViewSet(ModelViewSet):
    serializer_class = CourseStudentSerializer
    queryset = Notes.objects.all()
    permission_classes = (IsAuthenticated, )
    

class NotesCreateAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        serializer = NotesSerializer(data=request.data)
        if serializer.is_valid():
            notes = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class MyCoursesStudentViewSet(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = InfoStudentSerializer
    model = serializer_class.Meta.model

    # def get_serializer_class(self):
    #     if self.action == 'retrieve' or self.action == 'list':
    #         return InfoStudentSerializer
    #     return NotesSerializer

    def get_queryset(self):
            user = self.kwargs['pk']
            queryset = self.model.objects.filter(student__pk=user)
            return queryset
