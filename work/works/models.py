from django.db import models

# Create your models here.
#房源表
class Houses(models.Model):
    tltie=models.CharField(max_length=54)
    rurl=models.CharField(max_length=54)
    radd=models.CharField(max_length=54)
    geren=models.CharField(max_length=54)
    money=models.CharField(max_length=54)

#工作源表
class Jobs(models.Model):
    position=models.CharField(max_length=54)
    company=models.CharField(max_length=54)
    sadd=models.CharField(max_length=54)
    salary=models.CharField(max_length=54)
    claim=models.CharField(max_length=54)
    joburl=models.CharField(max_length=54)