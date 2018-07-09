from django.shortcuts import render, redirect

from lists.models import Item


# TODO: Display multiple items in the table
# TODO: Support more than one list
def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item-text'])
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'lists/home.html', {'items': items})
