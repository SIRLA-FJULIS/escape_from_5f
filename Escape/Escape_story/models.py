from django.db import models

class Flag(models.Model):
    ans = models.TextField(null=True)
    checkpoint = models.TextField(null=True)

class User_table(models.Model):
    user = models.CharField(max_length=100,null=True)
    password = models.CharField(max_length=100,null=True)