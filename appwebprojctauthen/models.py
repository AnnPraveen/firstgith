from django.contrib.auth.models import User
import email
from email.headerregistry import Address
from django.db import models
# Create your models here.
class course(models.Model):
    course_name=models.CharField(max_length=255) 
    course_fee=models.IntegerField()
   # def_str_(self):
    # return self.course_name

class student(models.Model):
    student_name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    age=models.IntegerField()
    joindate=models.IntegerField()
    course_id= models.ForeignKey(course,on_delete=models.CASCADE,null='TRUE')
