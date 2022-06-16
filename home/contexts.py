from .models import Topic


def topic(request):
    topics = Topic.objects.all()
    context = {'topics': topics}
    return context