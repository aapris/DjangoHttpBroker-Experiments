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


class RfidTag(models.Model):
    tagid = models.CharField(db_index=True, max_length=256)
    name = models.CharField(max_length=256, blank=True)
    reads = models.ManyToManyField('RfidScanner',
                                   blank=True,
                                   through="RfidRead",
                                   related_name="related_rfidtags",
                                   verbose_name="RFID Tag reads")

    def __str__(self):
        return f'{self.tagid} {self.name}'


class RfidRead(models.Model):
    rfidscanner = models.ForeignKey(RfidScanner, on_delete=models.CASCADE)
    rfidtag = models.ForeignKey(RfidTag, on_delete=models.CASCADE)
    scanned_at = models.DateTimeField(auto_now_add=True)
