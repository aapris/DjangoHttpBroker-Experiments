from django.db import models


class RfidScanner(models.Model):
    devid = models.CharField(db_index=True, unique=True, max_length=32)
    name = models.CharField(max_length=256, blank=True)
    description = models.CharField(max_length=10000, blank=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    activity_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.devid} ({self.name})'


class RfidRead(models.Model):
    rfidscanner = models.ForeignKey(RfidScanner, on_delete=models.CASCADE)
    tagid = models.CharField(db_index=True, max_length=256)
    scanned_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f'{self.datalogger} -> {self.forward}'
