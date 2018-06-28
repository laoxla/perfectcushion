from .models import Category


def menu_links(reqeuest):
    links = Category.objects.all()
    return dict(links=links)
