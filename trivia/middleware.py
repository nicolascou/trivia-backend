from django.http import HttpResponseForbidden

class RefererMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        referer = request.META.get('HTTP_REFERER')
        if referer is None or not referer.startswith('https://nicolascou.github.io'):
            return HttpResponseForbidden()
        response = self.get_response(request)
        return response