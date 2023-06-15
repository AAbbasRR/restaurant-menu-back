from django.http import (
    HttpResponseServerError,
    HttpResponseNotFound,
    JsonResponse
)
from django.utils.translation import gettext as _


def custom_404_response(request, exception):
    return HttpResponseNotFound(JsonResponse({
        "detail": _('URL Not Found.')
    }))


def custom_500_response(request):
    return HttpResponseServerError(JsonResponse({
        "detail": _('Server Error.')
    }))
