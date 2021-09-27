from shop.models import Contact, Product
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
import datetime
# Create your views here.


def index(request):
    products = Product.objects.all()
    params = {'product': products}
    return render(request, "shop/index.html", params)


def about(request):
    return render(request, "shop/about.html")


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, subject=subject,
                          desc=message, pubdate=datetime.date.today())
        contact.save()

    return render(request, "shop/contact.html")


def tracker(request):
    return render(request, "shop/index.html")


def productview(request, id):
    product = Product.objects.filter(id=id)

    return render(request, "shop/productview.html", {'product': product[0]})


def checkout(request):
    return render(request, "shop/index.html")


def search(request):
    return render(request, "shop/index.html")
