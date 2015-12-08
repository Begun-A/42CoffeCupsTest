from .models import RequestLog


class RequestLogMiddleware(object):
    def process_request(self, request):
        if not request.is_ajax():
            RequestLog(
                method=request.method,
                path=request.path,
                remote_addr=request.META['REMOTE_ADDR'],
            ).save()
        return None
