from . models import Centers


def menu_links(request):
    links = Centers.objects.all()
    return dict(links=links)
