from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # username = models.CharField(max_length=40,unique= True)
    phone = models.CharField(max_length=20, blank=True)
    full_name = models.CharField(max_length=250, blank=True)
    address = models.CharField(max_length=500, null=True)
    dob = models.DateField(null=True)
    registeration = models.DateField(auto_now_add=True)
    picture = models.FileField()

    def __str__(self):
        return self.full_name

class Student(User):
    grade = models.IntegerField()
    sub_grade = models.CharField(max_length=1)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.full_name


class Teacher(User):
    objects = User()

    def __str__(self):
        return self.full_name

    class Meta:
        proxy = True

class Lesson(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Log(models.Model):
    lesson     = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student    = models.ForeignKey(Student, on_delete=models.CASCADE)
    date       = models.DateTimeField()
    time_stamp = models.DateTimeField(auto_now=True)
    note       = models.TextField()

    def __str__(self):
        return self.student.full_name

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'

class GroupLog(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True)
    grade  = models.IntegerField()
    note   = models.TextField()
    time_stamp = models.DateField(auto_now=True)

    def __str__(self):
        return "{}".format(self.lesson)

    class Meta:
        verbose_name = 'General Note'
        verbose_name_plural = 'General Notes'


class Mark(models.Model):
    lesson     = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student    = models.ForeignKey(Student, on_delete=models.CASCADE)
    mark       = models.IntegerField()
    note       = models.TextField()
    tag        = models.CharField(max_length=200)
    date       = models.DateField()
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "grade for {} in {}".format(self.student, self.lesson)

    class Meta:
        verbose_name = 'Mark'
        verbose_name_plural = 'Marks'
