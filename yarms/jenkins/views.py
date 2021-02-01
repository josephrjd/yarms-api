from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, you have reached jenkins module.")