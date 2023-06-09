from rest_framework import viewsets
from .serializers import UserSerializer
from utils.page import BaseNumberPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from django.http import JsonResponse
from .filter import Filter
from rest_framework.exceptions import APIException
from django.contrib.auth import get_user_model

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    ordering_fields = ['id', "create_time", "update_time", ]

    def get_project(self):
        try:
            data_id = self.kwargs.get('pk')
            return data_id
        except:
            return None

    def get_queryset(self):
        data_id = self.get_project()
        if self.request.user:
            if data_id is None:
                return User.objects.filter(is_delete=False)
            else:
                return User.objects.filter(is_delete=False, id=data_id)
        else:
            return User.objects.none()

    def create(self, request, *args, **kwargs):
        data = self.request.data
        if User.objects.filter(username=data['username']).exists():
            raise APIException({"detail": "User exists"})
        else:
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=200, headers=headers)

    def destroy(self, request, pk, **kwargs):
        qs = self.get_object()
        qs.is_delete = True
        qs.save()
        serializer = self.get_serializer(qs, many=False)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=200, headers=headers)