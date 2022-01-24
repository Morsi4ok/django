import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def posts_index(request):
    result = ""
    user = User.objects.get(username=request.GET.get("author","morsik"))
    author_name = request.GET.get("author","morsik")
    for x in Post.objects.filter(author__username=author_name).order_by("-id")

    return HttpResponse(result)
