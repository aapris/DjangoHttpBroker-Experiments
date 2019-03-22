from django.contrib import admin
from .models import RfidScanner, RfidRead


class RfidScannerAdmin(admin.ModelAdmin):
    list_display = ('devid', 'name', 'activity_at', 'created_at')


admin.site.register(RfidScanner, RfidScannerAdmin)


class RfidReadAdmin(admin.ModelAdmin):
    list_display = ('rfidscanner', 'tagid', 'scanned_at')


admin.site.register(RfidRead, RfidReadAdmin)

