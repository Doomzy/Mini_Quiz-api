import re
from django.http.response import HttpResponse, JsonResponse

from .serializers import *

from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view, permission_classes

@api_view(['POST'])
@permission_classes((IsAdminUser, ))
def create(request):
    userSerlialized= UserSerializer(data= request.data)
    if userSerlialized.is_valid():
        studentSerialized= StudentSerializer(data= request.data)
        print(request.data)
        if studentSerialized.is_valid():
            userSerlialized.save()
            studentUser= User.objects.get(username= userSerlialized.data['username'])
            studentSerialized.save(user= studentUser)
            return JsonResponse(studentSerialized.data, status=status.HTTP_201_CREATED)
    return HttpResponse(status= status.HTTP_400_BAD_REQUEST)