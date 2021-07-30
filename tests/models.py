from django.db import models
from django.db.models.deletion import CASCADE
from students.models import Student
from subjects.models import Question, Subject

class Test(models.Model):
    student= models.ForeignKey(Student, default=None, on_delete=CASCADE)
    subject= models.ForeignKey(Subject, default=None, on_delete=CASCADE)
    grade= models.IntegerField(default=0)

    def __str__(self) :
        return (self.subject.name + " > " + self.student.name)

class Answer(models.Model):
    student= models.ForeignKey(Student, default=None, on_delete=CASCADE)
    test= models.ForeignKey(Test, default=None, on_delete=CASCADE)
    question= models.ForeignKey(Question, default=None, on_delete=CASCADE)
    chosen_answer= models.CharField(max_length=200, null= True)
    correct_answer= models.CharField(max_length=200) 
    correct= models.BooleanField(default=False)

    def __str__(self) :
        return (self.question.content + " > " + self.student.name)
