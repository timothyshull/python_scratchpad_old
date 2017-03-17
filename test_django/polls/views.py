from django.http import HttpResponse


def index(request):
    return HttpRequest("Hello, world. You're at the polls index.")
