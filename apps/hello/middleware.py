from .models import RequestLog


class RequestLogMiddleware(object):
    def process_request(self, request):
        if request.is_ajax():
            return None
        RequestLog(
            method=request.method,
            path=request.path,
            remote_addr=request.META['REMOTE_ADDR'],
        ).save()
        return None
