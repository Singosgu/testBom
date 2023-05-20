from django.urls import path, re_path
from . import views

urlpatterns = [
path(r'', views.API1ViewSet.as_view({"get": "list", "post": "create"}), name="api1"),
re_path(r'^(?P<pk>\d+)/$', views.API1ViewSet.as_view({
    'get': 'retrieve',
    'post': 'update',
    'delete': 'destroy'
}), name="api1_1")
]
