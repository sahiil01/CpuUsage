from django.contrib import admin
from .models import CpuData

# Register your models here.


@admin.register(CpuData)
class CPUdataAdmin(admin.ModelAdmin):
    list_display = ["id", "core1", "core2", "core3", "core4", "cpuSpeed", "ramUsage"]
