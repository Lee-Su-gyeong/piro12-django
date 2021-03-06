import logging
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Item

logger = logging.getLogger(__name__)  # __name__ => "shop.views"


def archives_year(request, year):
    return HttpResponse('{}년도에 대한 기록'.format(year))


def item_list(request):
    qs = Item.objects.all()

    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(name__icontains=q)

    logger.debug('query : {}'.format(q))

    return render(request, 'shop/item_list.html', {
        'item_list': qs,
        'q': q,
    })


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'shop/item_detail.html', {
        'item': item,
    })

