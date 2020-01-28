from django.db import models


class Flower(models.Model):
    name = models.CharField(max_length=30, null=False)
    color = models.CharField(max_length=30)
    quantity = models.IntegerField(null=True)

    class Meta:
        db_table = 'flowers'

    def __str__(self):
        return self


class Bunch(models.Model):
    name = models.CharField(max_length=30, null=False)
    flower = models.ManyToManyField(Flower, through='BunchContent')

    class Meta:
        db_table = 'bunches'

    def __str__(self):
        return self


class BunchContent(models.Model):
    flower = models.ForeignKey(Bunch, on_delete=models.CASCADE)
    bunch = models.ForeignKey(Flower, on_delete=models.CASCADE)
    f_quantity = models.IntegerField(null=True)

    class Meta:
        db_table = 'bunch_content'
