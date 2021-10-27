from django.db import models
from django.contrib.auth.models import AbstractUser

# class Instructor(AbstractUser):
#     pass 
#     # contentId=models.ForeignKey(Content,on_delete=models.CASCADE)   
class Preference(models.Model):
    siteLang=models.CharField(max_length=200)
    startLevel=models.CharField(max_length=20)
    currLevel=models.CharField(max_length=20)
    accountType=models.CharField(max_length=200)
class Content(models.Model):
    contentValue=models.TextField()
    contentImage=models.ImageField(upload_to='media/',height_field=None,width_field=None,max_length=100)
    contentAudio=models.FileField(upload_to='media/',max_length=100)
    contentVideo=models.FileField(upload_to='media/',max_length=100)
    isComplete=models.BooleanField()
    # createdBy=models.ForeignKey(Instructor,on_delete=models.CASCADE)
class Course(models.Model):
    courseName=models.CharField(max_length=200)
    courseDescription=models.TextField()
    contents=models.ForeignKey(Content,on_delete=models.CASCADE)
    def __str__(self):
        return self.courseName

class Quiz(models.Model):
    marks=models.IntegerField()
    courseId=models.ForeignKey(Course,on_delete=models.CASCADE)
    questionDir=models.FilePathField(path='C:/Users/Dires/project/language_project/Questions', max_length=100)
    answerDir=models.FilePathField(path='C:/Users/Dires/project/language_project/Answers',max_length=100)
    scored=models.IntegerField()

class Certificate(models.Model):
    certDate=models.DateField(auto_now_add=True)
    certUrl=models.URLField(max_length=200)
    courseId=models.OneToOneField(Course,on_delete=models.CASCADE)

class Grade(models.Model):
    courseId=models.ForeignKey(Course,on_delete=models.CASCADE)
    grade=models.IntegerField()
class CustomUser(AbstractUser):

    prefId=models.ForeignKey(Preference,on_delete=models.CASCADE,null=True,	blank=True)
    courseId=models.ForeignKey(Course,on_delete=models.CASCADE)
    quizId=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    certId=models.OneToOneField(Certificate,on_delete=models.CASCADE)
    gradeId=models.ForeignKey(Grade,on_delete=models.CASCADE)