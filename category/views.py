from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response

from category.models import Category

from category.serializers import CategorySerializer
# import json
from rest_framework import generics, permissions

from category import serializers


class CategoryCreateLIstViews(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategoryListSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser]

class CategoryDetailViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser]

# @api_view(['GET'])
# def tasks_list(request):
#     queryset = Category.objects.all()
#     serializer = CategorySerializer(instance=queryset, many=True)
#     return Response(serializer.data, status=200)
#
#
# @api_view(['GET', 'POST'])
# def categories_create(request):
#     if request.method == 'GET':
#         queryset = Category.objects.all()
#         serializer = CategorySerializer(instance=queryset, many=True)
#         return Response(serializer.data, status=200)
#
#     if request.method == 'POST':
#         data = request.data
#         serializer = CategorySerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=201)
