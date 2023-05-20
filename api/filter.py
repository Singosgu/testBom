from django_filters import FilterSet
from .models import API1Model


class API1filter(FilterSet):
    class Meta:
        model = API1Model
        fields = "__all__"
        exclude = ['permission', ]
