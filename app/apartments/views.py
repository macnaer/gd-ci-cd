from django.shortcuts import render, redirect
from .models import Apartments, ApartmentType
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.urls import reverse


def index(request):
    apartments = Apartments.objects.order_by(
        '-list_date').filter(is_published=True)
    # check if this is search request
    if 'city' in request.GET:
        city = request.GET['city']
        if city is not None:
            # print("city:", type(city), city)
            apartments = apartments.filter(city__iexact=city)
    
    paginator = Paginator(apartments, 2)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    
    context = {
        "apartments": page,
        "header_h1": "Квартири <span>для вас</span>",
        "header_p": "Головна >> Квартири для вас",
    }
    return render(request, "pages/apartments.html", context)


def apartment(request, apartment_id):
    apartment = get_object_or_404(Apartments, pk=apartment_id)
    context = {
        "apartment": apartment,
        "header_h1": "Квартири <span>для вас</span>",
        "header_p": "Головна >> Квартири для вас",
        "in_favorits": request.user in apartment.favorits.all(),
    }
    return render(request, "pages/apartment.html", context)


def search(request):
    apartments_list = Apartments.objects.order_by(
        '-list_date').filter(is_published=True)
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            apartments_list = apartments_list.filter(city__iexact=city)
    print("list: ", apartments_list)
    context = {
        "apartments_list": apartments_list,
        "header_h1": "Пошук",
        "header_p": "Головна >> Пошук",
    }
    return render(request, "pages/search.html", context)


def favorits(request):
    if request.method == "POST":
        apartment_id = request.POST['apartment_id']
        action = request.POST['action']
        if request.user != 'AnonymousUser':
            apartment = get_object_or_404(Apartments, pk=apartment_id)
            if action == 'add':
                if request.user not in apartment.favorits.all():
                    apartment.favorits.add(request.user)
            if action == 'delete':
                if request.user in apartment.favorits.all():
                    apartment.favorits.remove(request.user)
        return redirect(reverse("apartment", kwargs={"apartment_id": apartment_id}))
    return redirect("apartments")
