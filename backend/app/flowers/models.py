from django.db import models


class Flower(models.Model):
    type = models.CharField(max_length=30)
    color = models.CharField(max_length=30)

    class Meta:
        db_table = 'flowers'
