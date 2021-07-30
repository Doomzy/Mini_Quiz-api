from django.db import models
from django.db.models.deletion import CASCADE

class Subject(models.Model):

    ayChoices=[
        ('1','1st'),
        ('2','2nd'),
        ('3','3rd')
    ]
    name= models.CharField(max_length=100)
    academic_year= models.CharField(choices=ayChoices, max_length=3)

    def __str__(self):
        return self.name

class Question(models.Model):
    subject= models.ForeignKey(Subject, default= None, on_delete=CASCADE)
    content= models.TextField(max_length=5000)
    ans1= models.CharField(max_length=200)
    ans2= models.CharField(max_length=200)
    ans3= models.CharField(max_length=200)
    ans4= models.CharField(max_length=200)
    correct_answer= models.CharField(max_length=200)

    def __str__(self):
        return self.content