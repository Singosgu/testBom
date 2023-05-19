from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework.exceptions import APIException

from utils.auth import Authorization
from utils.permission import BasePermission, BaseAllowAny
from utils.page import BaseNumberPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filter import API1filter


from django.contrib.auth import get_user_model

User = get_user_model()


class APIViewSet(viewsets.ModelViewSet):
    authentication_classes = [Authorization, ]
    permission_classes = [BasePermission, BaseAllowAny, ]
    pagination_class = BaseNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    filter = API1filter

    def __init__(self):
        self.query = None

    def get_project(self):
        try:
            data_id = self.kwargs.get('pk')
            return data_id
        except:
            return None

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
        data = self.request.data
        data['openid'] = self.request.auth.openid
        if DemoModel.objects.filter(openid=data['openid'], bin_size=data['bin_size'], is_delete=False).exists():
            raise APIException({"detail": "Data exists"})
        else:
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=200, headers=headers)

    def update(self, request, pk):
        qs = self.get_object()
        if qs.openid != self.request.auth.openid:
            raise APIException({"detail": "Cannot update data which not yours"})
        else:
            data = self.request.data
            serializer = self.get_serializer(qs, data=data)
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
