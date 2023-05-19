from django.db import models
from django.conf import settings


class BaseModel(models.Model):
    license = models.CharField(default='', max_length=255, help_text="license", verbose_name="license")
    is_delete = models.BooleanField(default=False, help_text="Is Delete", verbose_name="Is Delete")
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True, help_text="Update Time",
                                       verbose_name="Update Time")
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, help_text="Create Time",
                                       verbose_name="Create Time")
    permission = models.JSONField(default=dict, help_text="permission", verbose_name="permission")
    char1 = models.CharField(default='', max_length=255, help_text="char1", verbose_name="char1")
    char2 = models.CharField(default='', max_length=255, help_text="char2", verbose_name="char2")
    char3 = models.CharField(default='', max_length=255, help_text="char3", verbose_name="char3")
    char4 = models.CharField(default='', max_length=255, help_text="char4", verbose_name="char4")
    char5 = models.CharField(default='', max_length=255, help_text="char5", verbose_name="char5")
    char6 = models.CharField(default='', max_length=255, help_text="char6", verbose_name="char6")
    char7 = models.CharField(default='', max_length=255, help_text="char7", verbose_name="char7")
    char8 = models.CharField(default='', max_length=255, help_text="char8", verbose_name="char8")
    char9 = models.CharField(default='', max_length=255, help_text="char9", verbose_name="char9")
    char10 = models.CharField(default='', max_length=255, help_text="char10", verbose_name="char10")
    char11 = models.CharField(default='', max_length=255, help_text="char11", verbose_name="char11")
    char12 = models.CharField(default='', max_length=255, help_text="char12", verbose_name="char12")
    char13 = models.CharField(default='', max_length=255, help_text="char13", verbose_name="char13")
    char14 = models.CharField(default='', max_length=255, help_text="char14", verbose_name="char14")
    char15 = models.CharField(default='', max_length=255, help_text="char15", verbose_name="char15")
    char16 = models.CharField(default='', max_length=255, help_text="char16", verbose_name="char16")
    char17 = models.CharField(default='', max_length=255, help_text="char17", verbose_name="char17")
    char18 = models.CharField(default='', max_length=255, help_text="char18", verbose_name="char18")
    char19 = models.CharField(default='', max_length=255, help_text="char19", verbose_name="char19")
    char20 = models.CharField(default='', max_length=255, help_text="char20", verbose_name="char20")
    char21 = models.CharField(default='', max_length=255, help_text="char21", verbose_name="char21")
    char22 = models.CharField(default='', max_length=255, help_text="char22", verbose_name="char22")
    char23 = models.CharField(default='', max_length=255, help_text="char23", verbose_name="char23")
    char24 = models.CharField(default='', max_length=255, help_text="char24", verbose_name="char24")
    char25 = models.CharField(default='', max_length=255, help_text="char25", verbose_name="char25")
    int1 = models.IntegerField(default=0, help_text="int1", verbose_name="int1")
    int2 = models.IntegerField(default=0, help_text="int2", verbose_name="int2")
    int3 = models.IntegerField(default=0, help_text="int3", verbose_name="int3")
    int4 = models.IntegerField(default=0, help_text="int4", verbose_name="int4")
    int5 = models.IntegerField(default=0, help_text="int5", verbose_name="int5")
    int6 = models.IntegerField(default=0, help_text="int6", verbose_name="int6")
    int7 = models.IntegerField(default=0, help_text="int7", verbose_name="int7")
    int8 = models.IntegerField(default=0, help_text="int8", verbose_name="int8")
    int9 = models.IntegerField(default=0, help_text="int9", verbose_name="int9")
    int10 = models.IntegerField(default=0, help_text="int10", verbose_name="int10")
    int11 = models.IntegerField(default=0, help_text="int11", verbose_name="int11")
    int12 = models.IntegerField(default=0, help_text="int12", verbose_name="int12")
    int13 = models.IntegerField(default=0, help_text="int13", verbose_name="int13")
    int14 = models.IntegerField(default=0, help_text="int14", verbose_name="int14")
    int15 = models.IntegerField(default=0, help_text="int15", verbose_name="int15")
    int16 = models.IntegerField(default=0, help_text="int16", verbose_name="int16")
    int17 = models.IntegerField(default=0, help_text="int17", verbose_name="int17")
    int18 = models.IntegerField(default=0, help_text="int18", verbose_name="int18")
    int19 = models.IntegerField(default=0, help_text="int19", verbose_name="int19")
    int20 = models.IntegerField(default=0, help_text="int20", verbose_name="int20")
    int21 = models.IntegerField(default=0, help_text="int21", verbose_name="int21")
    int22 = models.IntegerField(default=0, help_text="int22", verbose_name="int22")
    int23 = models.IntegerField(default=0, help_text="int23", verbose_name="int23")
    int24 = models.IntegerField(default=0, help_text="int24", verbose_name="int24")
    int25 = models.IntegerField(default=0, help_text="int25", verbose_name="int25")
    float1 = models.FloatField(default=0, help_text="float1", verbose_name="float1")
    float2 = models.FloatField(default=0, help_text="float2", verbose_name="float2")
    float3 = models.FloatField(default=0, help_text="float3", verbose_name="float3")
    float4 = models.FloatField(default=0, help_text="float4", verbose_name="float4")
    float5 = models.FloatField(default=0, help_text="float5", verbose_name="float5")
    float6 = models.FloatField(default=0, help_text="float6", verbose_name="float6")
    float7 = models.FloatField(default=0, help_text="float7", verbose_name="float7")
    float8 = models.FloatField(default=0, help_text="float8", verbose_name="float8")
    float9 = models.FloatField(default=0, help_text="float9", verbose_name="float9")
    float10 = models.FloatField(default=0, help_text="float10", verbose_name="float10")
    float11 = models.FloatField(default=0, help_text="float11", verbose_name="float11")
    float12 = models.FloatField(default=0, help_text="float12", verbose_name="float12")
    float13 = models.FloatField(default=0, help_text="float13", verbose_name="float13")
    float14 = models.FloatField(default=0, help_text="float14", verbose_name="float14")
    float15 = models.FloatField(default=0, help_text="float15", verbose_name="float15")
    float16 = models.FloatField(default=0, help_text="float16", verbose_name="float16")
    float17 = models.FloatField(default=0, help_text="float17", verbose_name="float17")
    float18 = models.FloatField(default=0, help_text="float18", verbose_name="float18")
    float19 = models.FloatField(default=0, help_text="float19", verbose_name="float19")
    float20 = models.FloatField(default=0, help_text="float20", verbose_name="float20")
    float21 = models.FloatField(default=0, help_text="float21", verbose_name="float21")
    float22 = models.FloatField(default=0, help_text="float22", verbose_name="float22")
    float23 = models.FloatField(default=0, help_text="float23", verbose_name="float23")
    float24 = models.FloatField(default=0, help_text="float24", verbose_name="float24")
    float25 = models.FloatField(default=0, help_text="float25", verbose_name="float25")
    bool1 = models.BooleanField(default=False, help_text="bool1", verbose_name="bool1")
    bool2 = models.BooleanField(default=False, help_text="bool2", verbose_name="bool2")
    bool3 = models.BooleanField(default=False, help_text="bool3", verbose_name="bool3")
    bool4 = models.BooleanField(default=False, help_text="bool4", verbose_name="bool4")
    bool5 = models.BooleanField(default=False, help_text="bool5", verbose_name="bool5")
    bool6 = models.BooleanField(default=False, help_text="bool6", verbose_name="bool6")
    bool7 = models.BooleanField(default=False, help_text="bool7", verbose_name="bool7")
    bool8 = models.BooleanField(default=False, help_text="bool8", verbose_name="bool8")
    bool9 = models.BooleanField(default=False, help_text="bool9", verbose_name="bool9")
    bool10 = models.BooleanField(default=False, help_text="bool10", verbose_name="bool10")
    bool11 = models.BooleanField(default=False, help_text="bool11", verbose_name="bool11")
    bool12 = models.BooleanField(default=False, help_text="bool12", verbose_name="bool12")
    bool13 = models.BooleanField(default=False, help_text="bool13", verbose_name="bool13")
    bool14 = models.BooleanField(default=False, help_text="bool14", verbose_name="bool14")
    bool15 = models.BooleanField(default=False, help_text="bool15", verbose_name="bool15")
    bool16 = models.BooleanField(default=False, help_text="bool16", verbose_name="bool16")
    bool17 = models.BooleanField(default=False, help_text="bool17", verbose_name="bool17")
    bool18 = models.BooleanField(default=False, help_text="bool18", verbose_name="bool18")
    bool19 = models.BooleanField(default=False, help_text="bool19", verbose_name="bool19")
    bool20 = models.BooleanField(default=False, help_text="bool20", verbose_name="bool20")
    bool21 = models.BooleanField(default=False, help_text="bool21", verbose_name="bool21")
    bool22 = models.BooleanField(default=False, help_text="bool22", verbose_name="bool22")
    bool23 = models.BooleanField(default=False, help_text="bool23", verbose_name="bool23")
    bool24 = models.BooleanField(default=False, help_text="bool24", verbose_name="bool24")
    bool25 = models.BooleanField(default=False, help_text="bool25", verbose_name="bool25")
    text1 = models.TextField(default='', help_text="text1", verbose_name="text1")
    text2 = models.TextField(default='', help_text="text2", verbose_name="text2")
    text3 = models.TextField(default='', help_text="text3", verbose_name="text3")
    text4 = models.TextField(default='', help_text="text4", verbose_name="text4")
    text5 = models.TextField(default='', help_text="text5", verbose_name="text5")
    text6 = models.TextField(default='', help_text="text6", verbose_name="text6")
    text7 = models.TextField(default='', help_text="text7", verbose_name="text7")
    text8 = models.TextField(default='', help_text="text8", verbose_name="text8")
    text9 = models.TextField(default='', help_text="text9", verbose_name="text9")
    text10 = models.TextField(default='', help_text="text10", verbose_name="text10")
    text11 = models.TextField(default='', help_text="text11", verbose_name="text11")
    text12 = models.TextField(default='', help_text="text12", verbose_name="text12")
    text13 = models.TextField(default='', help_text="text13", verbose_name="text13")
    text14 = models.TextField(default='', help_text="text14", verbose_name="text14")
    text15 = models.TextField(default='', help_text="text15", verbose_name="text15")
    text16 = models.TextField(default='', help_text="text16", verbose_name="text16")
    text17 = models.TextField(default='', help_text="text17", verbose_name="text17")
    text18 = models.TextField(default='', help_text="text18", verbose_name="text18")
    text19 = models.TextField(default='', help_text="text19", verbose_name="text19")
    text20 = models.TextField(default='', help_text="text20", verbose_name="text20")
    text21 = models.TextField(default='', help_text="text21", verbose_name="text21")
    text22 = models.TextField(default='', help_text="text22", verbose_name="text22")
    text23 = models.TextField(default='', help_text="text23", verbose_name="text23")
    text24 = models.TextField(default='', help_text="text24", verbose_name="text24")
    text25 = models.TextField(default='', help_text="text25", verbose_name="text25")
    
    
    class Meta:
        abstract = True
        verbose_name = settings.BASE_DB_TABLE + ' Base Model'
        verbose_name_plural = verbose_name