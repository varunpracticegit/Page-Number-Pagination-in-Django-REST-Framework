from django.shortcuts import render
from .models import Student
from api.serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from api.mypaginations import MyPageNumberPagination

# Create your views here.
class StudentAPI(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyPageNumberPagination