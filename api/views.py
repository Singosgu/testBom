from utils.views import BaseViewSet
from .filter import API1filter
from .models import API1Model


class API1ViewSet(BaseViewSet):
    filter = API1filter

    def __init__(self):
        self.query = API1Model
