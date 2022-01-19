import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def homework_index(request):
    value = request.GET.get("key")
    logger.info(value)
    return HttpResponse("Homework index view")