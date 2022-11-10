from http import HTTPStatus

from django.http import HttpResponse


def index(request):
    return HttpResponse(status=HTTPStatus.OK)


def second_page(request):
    # return HttpResponse('А это вторая страница')
    # HTTPStatus.OK
    return HttpResponse(status=HTTPStatus.OK)
