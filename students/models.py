from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

from django.dispatch import receiver
from django.db.models.signals import pre_save

class Student(Model):

    ayChoices=[('1','1st'),('2','2nd'),('3','3rd')]

    user= models.ForeignKey(User, on_delete=CASCADE, default= None)
    name= models.CharField(max_length=100)
    student_id= models.IntegerField(primary_key=True)
    academic_year= models.CharField(choices=ayChoices, max_length=3)

    def __str__(self):
        return self.name

@receiver(pre_save, sender=Student)
def studentSave(sender, instance, **kwargs):
    if not instance.student_id:
        instance.student_id= instance.user.id
        
