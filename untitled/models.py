from django.db import models
from django.contrib.postgres.fields import *

class MyModel(models.Model):
    data = JSONField()

    def __str__(self):
        return self.data