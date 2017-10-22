from rest_framework import serializers
from .models import *

class StudentSeriaizer(serializers.ModelSerializer):
    """
    Student Api Serializer
    """
    class Meta:
        model = Student
        fields = ('first_name', 'full_name', 'last_name', 'dob', 'grade', 'sub_grade', 'username','password', 'email', 'phone', 'address', 'picture')

class TeacherSerializer():
    pass

class GradeSerializer():
    pass

class LogSerializer():
    pass

