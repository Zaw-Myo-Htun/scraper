from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models,checkwishlist


# Create your views here.
def home(request):
    wishlist_items = models.Wishlist.objects.all().order_by("-added_date")
    return render(request, 'my_app/index.html', {"wishlist_items":wishlist_items}) 

def add_wishlist(request):
    url = request.POST.get('url')
    item_name = request.POST.get('item_name')
    expected_price = request.POST.get('expected_price')
    models.Wishlist.objects.create(
        url = url,
        item_name = item_name,
        expected_price = float(expected_price)
    )
    #return render(request, 'my_app/index.html')  
    return HttpResponseRedirect("/")

def delete_wishlist(request, wishlist_id):
    models.Wishlist.objects.get(id=wishlist_id).delete()
    return HttpResponseRedirect("/")      


def check_wishlist(request):
    wishlist_items = models.Wishlist.objects.all().order_by("-added_date")
    
    for i in range(len(wishlist_items)):
        print("Item", (i+1))
        checkwishlist.check_price(wishlist_items[i].url, wishlist_items[i].expected_price) 

    return HttpResponseRedirect("/")
