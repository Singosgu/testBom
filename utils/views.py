from rest_framework import viewsets

from rest_framework.response import Response

from utils.auth import Authorization
from utils.permission import BasePermission, BaseAllowAny
from utils.page import BaseNumberPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


from django.contrib.auth import get_user_model

User = get_user_model()


class BaseViewSet(viewsets.ModelViewSet):
    authentication_classes = [Authorization, ]
    permission_classes = [BasePermission, BaseAllowAny, ]
    pagination_class = BaseNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]

    def __init__(self):
        self.query = None

    def get_project(self):
        try:
            data_id = self.kwargs.get('pk')
            return data_id
        except:
            return None

    def get_data(self):
        return self.request.data

    def get_queryset(self):
        data_id = self.get_project()
        if self.request.user:
            if id is None:
                return self.query.objects.filter(is_delete=False)
            else:
                return self.query.objects.filter(is_delete=False, id=data_id)
        else:
            return self.query.objects.none()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.get_data())
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=200, headers=headers)

    def update(self, request, pk):
        qs = self.get_object()
        serializer = self.get_serializer(qs, data=self.get_data())
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=200, headers=headers)

    def destroy(self, request, pk):
        qs = self.get_object()
        qs.is_delete = True
        qs.save()
        serializer = self.get_serializer(qs, many=False)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=200, headers=headers)
