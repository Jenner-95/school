from rest_framework import serializers
from evaluations.models import Course, Grade, Notes
from django.contrib.auth.models import User
from users.serializers import TeacherSerializer, StudentSerializer


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name']


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'


class CourseTeacherSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    grade = GradeSerializer()

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "teacher",
            "grade",
        ]

class CourseStudentSerializer(serializers.ModelSerializer):
    course = CourseNameSerializer()
    student = serializers.SerializerMethodField()

    class Meta:
        model = Notes
        fields = [
            "id",
            "course",
            "student",
        ]

    def student(self):
        return self.student.filter(profile__tipo=1).count()


class InfoStudentSerializer(serializers.ModelSerializer):
    course = CourseNameSerializer()

    class Meta:
        model = Notes
        fields = [
            "course",
            "score",
        ]