from django.shortcuts import render
from django.http.response import HttpResponse

from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response

from .serializers import RegisterSerializer
from .models import User
# Create your views here.

class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny,]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        token = Token.objects.create(user=serializer.instance)
        return Response({"token":token.key}, status=status.HTTP_201_CREATED)