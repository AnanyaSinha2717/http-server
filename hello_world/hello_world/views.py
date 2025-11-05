from django.http import HttpResponse


def index(request):
    return HttpResponse(
        'Hello snake from Django!\n',
        content_type='text/plain'
    )
