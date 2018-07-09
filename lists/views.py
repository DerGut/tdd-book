from django.shortcuts import render, redirect

from lists.models import Item


# TODO: Display multiple items in the table
# TODO: Support more than one list
def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item-text'])
        return redirect('/lists/the-only-list-in-the-world/')

    return render(request, 'lists/home.html')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'lists/list.html', {'items': items})
