from django.shortcuts import render
from . models import MovieData
from . serializers import MovieSerializer
from rest_framework import viewsets
from . pagination import CustomPagination
from rest_framework.filters import SearchFilter,OrderingFilter
# Create your views here.

class movieApi(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer
    pagination_class = CustomPagination
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['name','actors','geners']
    ordering_fields = ['name']
