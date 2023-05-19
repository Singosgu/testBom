from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from guardian.shortcuts import assign_perm


class User(AbstractUser):
    type = models.IntegerField(default=1, verbose_name="User Type")
    phone = models.CharField(default='', max_length=255, blank=True, verbose_name="Phone")
    error_login = models.IntegerField(default=0, verbose_name="Error Login Time")
    is_delete = models.BooleanField(default=False, verbose_name="Delete Label")
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Update Time")

    class Meta(AbstractUser.Meta):
        db_table = settings.BASE_DB_TABLE + '_user'
        verbose_name = settings.BASE_DB_TABLE + ' User'
        verbose_name_plural = verbose_name
        ordering = ['-id']
        permissions = ()
