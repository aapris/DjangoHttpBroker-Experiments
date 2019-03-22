import datetime
from django.conf import settings
from django.http.response import HttpResponse
from broker.providers.endpoint import EndpointProvider
from experiments.models import RfidScanner, RfidRead
from broker.utils import basicauth


class RfidEndpoint(EndpointProvider):
    description = 'Receive scanned RFID tags from ESP8266'

    def handle_request(self, request):
        # now = datetime.datetime.utcnow()
        devid = request.GET.get('devid')
        tagid = request.GET.get('tagid')
        if tagid is None or devid is None:
            return HttpResponse('tagid and devid are mandatory GET parameters', status=400)
        rs, created = RfidScanner.objects.get_or_create(devid=devid)
        rr = RfidRead(rfidscanner=rs, tagid=tagid)
        rr.save()
        print(devid, tagid)
        return HttpResponse('OK', content_type='text/plain')
