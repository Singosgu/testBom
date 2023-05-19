from django_filters import FilterSet
from .models import api1


class API1filter(FilterSet):
    class Meta:
        model = api1
        fields = "__all__"
        exclude = []
