from django.db import models


class Wards(models.Model):
    name=models.CharField(max_length=50,blank=True,null=None)
    no=models.IntegerField(unique=True,blank=True,null=None)
