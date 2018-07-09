from django.shortcuts import render, redirect

from lists.models import Item, List


# TODO: Support more than one list
def home_page(request):
    return render(request, 'lists/home.html')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'lists/list.html', {'items': items})


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item-text'], list=list_)
    return redirect('/lists/the-only-list-in-the-world/')