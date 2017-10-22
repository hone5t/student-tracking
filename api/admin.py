from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


@admin.register(User)
class customUserAdmin(UserAdmin):
    icon = '<i class="material-icons">people_outline</i>'

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">perm_identity</i>'

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    name = 'Student'
    fields = ('first_name', 'full_name', 'last_name', 'dob', 'grade', 'sub_grade', 'username','password', 'email', 'phone', 'address', 'picture')
    icon = '<i class="material-icons">face</i>'


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">library_books</i>'

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">speaker_notes</i>'

@admin.register(GroupLog)
class GroupLogAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">announcement</i>'

@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">assessment</i>'

# using decorator seems better
# admin.site.register(User, customUserAdmin)
# admin.site.register(Teacher, TeacherAdmin)
# admin.site.register(Student, StudentAdmin)
# admin.site.register(Lesson, LessonAdmin)
# admin.site.register(Log, LogAdmin)
