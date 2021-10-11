from django.shortcuts import render
from .models import Tutor
from .serializers import TutorSerializer
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser


# Create your views here.


@api_view(['POST'])
def create_tutor(request):
    data = JSONParser.parse(request)
    user = User.objects.create_user(username=data['email'], email=data['email'], password=data['password'])
    data['user_id'] = user.pk
    serializer = TutorSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_object(pk):
    try:
        return Tutor.objects.get(pk=pk)
    except Tutor.DoesNotExist:
        raise Http404


@api_view(['GET'])
def get_tutor(request, pk):
    tutor = get_object(pk)
    serializer = TutorSerializer(tutor)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def edit_tutor(request):
    pass