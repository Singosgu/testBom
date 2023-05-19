from django.conf import settings
from utils.db import BaseModel


class api1(BaseModel):
    class Meta:
        db_table = settings.BASE_DB_TABLE + '_api1'
        verbose_name = settings.BASE_DB_TABLE + ' API1'
        verbose_name_plural = verbose_name
        ordering = ['-id']
