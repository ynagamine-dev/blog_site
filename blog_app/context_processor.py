from .models import Tag


def tag_renderer(request):
    return{
        'tag_list': Tag.objects.all(),
    }
