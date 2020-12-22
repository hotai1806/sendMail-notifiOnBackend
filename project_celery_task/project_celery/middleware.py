from django.utils.deprecation import MiddlewareMixin

hosts = {
    "localhost:8000": "tasks.urls",
    "domain1:8000": "tasks.urls",
    "domain2:8000": "helloworld.urls",
}


class SimpleMiddleWare(MiddlewareMixin):
    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):

        host = request.get_host()
        request.urlconf = hosts.get(host)
        response = self.get_response(request)
        return response
