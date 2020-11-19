from django.contrib import admin
from evaluations.models import Course, Grade, Notes
# Register your models here.

admin.site.register(Course)
admin.site.register(Grade)
admin.site.register(Notes)