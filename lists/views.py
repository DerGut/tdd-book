from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from lists.forms import EMPTY_ITEM_ERROR, ItemForm
from lists.models import Item, List


def home_page(request):
    return render(request, 'lists/home.html', context={'form': ItemForm()})


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    error = None

    if request.method == 'POST':
        try:
            item = Item(text=request.POST['item-text'], list=list_)
            item.full_clean()
            item.save()
            return redirect(list_)
        except ValidationError:
            error = EMPTY_ITEM_ERROR

    return render(request, 'lists/list.html', {'list': list_, 'error': error})


def new_list(request):
    list_ = List.objects.create()
    item = Item(text=request.POST['item-text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error_msg = EMPTY_ITEM_ERROR
        return render(request, 'lists/home.html', {'error': error_msg})
    return redirect(list_)
