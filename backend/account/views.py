from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http.response import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST, require_GET

from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response

from .serializers import UserSerializer
from .models import User
# Create your views here.

class RegisterView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny,]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        token = Token.objects.create(user=serializer.instance)
        return Response({"token":token.key}, status=status.HTTP_201_CREATED)


@method_decorator(require_POST, name="dispatch")
class LoginView(APIView):
    def post(self, request):
        user = authenticate(username=request.data["username"], password=request.data["password"])
        if user is not None:
            token, is_create = Token.objects.get_or_create(user=user)
            res_status = status.HTTP_201_CREATED if is_create else status.HTTP_200_OK
            return Response({"token": token.key}, status=res_status)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


@method_decorator(require_GET, name="dispatch")
class LogoutView(APIView):
    def get(self, request):
        user = request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


@method_decorator(require_GET, name="dispatch")
class UserDetailView(RetrieveAPIView):
    serializer_class = UserSerializer
    lookup_field = "username"
    queryset = User.objects.all()
