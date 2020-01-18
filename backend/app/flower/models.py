from django.db import models


class Flower(models.Model):
    name = models.CharField(max_length=30, null=False)
    color = models.CharField(max_length=30)

    class Meta:
        db_table = 'flowers'

    def __str__(self):
        return self
