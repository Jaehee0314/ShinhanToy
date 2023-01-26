from django.shortcuts import render

# Create your views here.
from rest_framework import generics, mixins, status
from .models import Member
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from .serializers import MemberSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class MemberRegisterView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    serializer_class = MemberSerializer
    
    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

class ChangePasswordView(APIView):  
    permission_classes = [IsAuthenticated]
    # 로그인한 사용자만 들어올 수 있는 곳
    def put(self, request, *args, **kwargs):
        current = request.data.get('current')
        password = request.data.get('password1')
        password2 = request.data.get('password2')

        if password != password2:
            return Response({
                'detail': 'Wrong new passwords',
            }, status=status.HTTP_400_BAD_REQUEST)

        member = request.user


        if not check_password(current, member.password):
            return Response({
                'detail': 'Wrong password',
            }, status=status.HTTP_400_BAD_REQUEST)

        member.password = make_password(password2)
        member.save()

        return Response(status=status.HTTP_200_OK)