from django.http.response import HttpResponse, JsonResponse
from rest_framework import  status

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser

from .models import Question, Subject

from .serializers import SubjectSerializer, CreateQuestionSerializer


@api_view(['POST'])
@permission_classes((IsAdminUser,))
#CREATE SUBJECT
def cSubject(request):
    #check if the subject exists
    if Subject.objects.filter(name= request.data['name']).exists():
        return HttpResponse('The subject already exists', status= status.HTTP_400_BAD_REQUEST)
    else:
        serializedSubject= SubjectSerializer(data= request.data)
        if serializedSubject.is_valid():
            serializedSubject.save()
            return JsonResponse(serializedSubject.data)
    return HttpResponse('somthing is wrong', status= status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((IsAdminUser,))
#DELETE SUBJECT
def dSubject(request):
    mySubject= Subject.objects.filter(name= request.data['name'])
    #check if the subject exists
    if not mySubject:
        return HttpResponse('Theres no such subject!', status= status.HTTP_400_BAD_REQUEST)  
    else:
        mySubject.delete()
        return HttpResponse("Subject Deleted!")  

@api_view(['POST'])
@permission_classes((IsAdminUser,))
#CREATE QUESTION
def cQuestion(request):
    serializedQuestion= CreateQuestionSerializer(data= request.data)
    if serializedQuestion.is_valid():
        serializedQuestion.save()
    return JsonResponse(serializedQuestion.data)


@api_view(['POST'])
@permission_classes((IsAdminUser,))
#DELETE QUESTION
def dQuestion(request):    
    myQuestion= Question.objects.filter(content= request.data['content'], subject= request.data['subject'])
    #check if the Question exists        
    if not myQuestion:
        return HttpResponse('Theres no such Question!', status= status.HTTP_400_BAD_REQUEST)  
    else:
        myQuestion.delete()
        return HttpResponse("Question Deleted!") 