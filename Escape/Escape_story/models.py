from django.db import models

class Flag(models.Model):
    ans = models.TextField(null=True)
    checkpoint = models.TextField(null=True)

