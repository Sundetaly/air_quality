from django.db import models


class City(models.Model):
    name = models.CharField(max_length=150)
    pollution_level_00 = models.DecimalField(max_digits=10, decimal_places=1)
    pollution_level_01 = models.DecimalField(max_digits=10, decimal_places=1)
    pollution_level_02 = models.DecimalField(max_digits=10, decimal_places=1)
    industries = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=250)
    count_pesticide = models.IntegerField()
    name_pesticide = models.CharField(max_length=250, blank=True, null=True)
    name_banned_pesticide = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name


class ImportRecord(models.Model):
    file = models.FileField(upload_to='files')