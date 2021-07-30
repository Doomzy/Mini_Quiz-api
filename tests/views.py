from django.http.response import HttpResponse, JsonResponse
from rest_framework import status

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Test, Answer
from subjects.models import Subject, Question
from students.models import Student
import random

from .serializers import TestSerializer, AnswerSerializer
from subjects.serializers import QuestionSerializer


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
#RETRIEVE TEST
def rTest(request, pk):

    #check if the subject exists
    try:
        mySubject= Subject.objects.get(id= pk)
    except: 
        return HttpResponse('Theres no such subject!', status= status.HTTP_404_NOT_FOUND)
    
    #subject exists
    myStudent= Student.objects.get(user= request.user)
    #check if the user and the subject have the same academic year
    if myStudent.academic_year == mySubject.academic_year:
        #check if the user already took the test
        if Test.objects.filter(student= myStudent, subject= mySubject).exists():
            return JsonResponse("you already took the test", safe= False)
        #user didnt take it , return questions
        else:
            myQuestionsId= Question.objects.values_list('id', flat= True)
            randomQuestions= random.sample(list(myQuestionsId), 3)
            myQuestions= Question.objects.filter(id__in= randomQuestions)
            SerializedQuestions= QuestionSerializer(myQuestions, many= True)
            return JsonResponse(SerializedQuestions.data, safe= False)
    #the user doesnt have the same academic year as the subject 
    else:
        return HttpResponse('you are not allowed to take this subject', status= status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
#SUBMIT TEST
def sTest(request, pk):

    #check if the subject exists
    try:
        mySubject= Subject.objects.get(id= pk)
    except: 
        return HttpResponse('Theres no such subject!', status= status.HTTP_404_NOT_FOUND)
    
    #subject exists
    myStudent= Student.objects.get(user= request.user)
    #check if the user and the subject have the same academic year
    if myStudent.academic_year == mySubject.academic_year:
        #check if the user already took the test
        if Test.objects.filter(student= myStudent, subject= mySubject).exists():
            return JsonResponse("you already took the test", safe= False)
        #user didnt take it, take the quistions in the request and create the test
        else:
            grade= 0
            myTest= Test()
            myTest.student= myStudent
            myTest.subject= mySubject
            myTest.save()

            for ans in request.data:

                myQuestion= Question.objects.get(id= ans['question_id'])

                myAnswer= Answer()
                myAnswer.student= myStudent
                myAnswer.chosen_answer= ans['chosen_answer']
                myAnswer.question= myQuestion
                myAnswer.correct_answer= myQuestion.correct_answer
                myAnswer.test= myTest
                myAnswer.save()

                if myAnswer.chosen_answer == myAnswer.correct_answer:
                    grade+=2
                    myAnswer.correct= True
                    myAnswer.save()
                
            myTest.grade= grade
            myTest.save()
            serializedTest= TestSerializer(myTest)
            
            return JsonResponse(serializedTest.data, safe= False)
    #the user doesnt have the same academic year as the subject 
    else:
        return HttpResponse('you are not allowed to take this subject', status= status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))

def retrieveResult(request, pk):
    try:
        mySubject= Subject.objects.get(id= pk)
    except: 
        return HttpResponse('Theres no such subject!', status= status.HTTP_404_NOT_FOUND)

    myStudent= Student.objects.get(user= request.user)
    myTest= Test.objects.filter(student= myStudent, subject= mySubject).first()
    if not myTest:
        return JsonResponse('you didnt take the test or you are not allowed to', safe= False)
    else:
        
        serializedTest= TestSerializer(myTest)
        myAnswers= Answer.objects.filter(student= myStudent, test= myTest)
        serializedAnswers= AnswerSerializer(myAnswers, many= True)

        return JsonResponse((serializedTest.data, serializedAnswers.data), safe= False)