from django.db import models

# Create your models here.


class CpuData(models.Model):
    core1 = models.CharField(max_length=20)
    core2 = models.CharField(max_length=20)
    core3 = models.CharField(max_length=20)
    core4 = models.CharField(max_length=20)
    cpuSpeed = models.CharField(max_length=20)
    ramUsage = models.CharField(max_length=20)
