from django.urls import path, include
from rest_framework import viewsets, generics
from .models import Category,Course
from .serializers import CategorySerializer, CourseSerializer


class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.filter(active=True)
    serializer_class = CategorySerializer

    def get_queryset(self):
        query = self.queryset

        kw = self.request.query_params.get('kw')

        if kw:
            query = query.filter(name__icontains=kw)

        return query

class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Course.oject.filter(active=True)
    serializer_class = CourseSerializer




