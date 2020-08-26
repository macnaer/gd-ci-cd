from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'pages/index.html')


def about(request):
    data = {"header_h1": "Про <span>Нас</span>",
            "header_p": "Головна >> Про нас"}
    return render(request, 'pages/about.html', context=data)


def guarantee(request):
    data = {"header_h1": "НАШІ <span>ГАРАНТІЇ</span>",
            "header_p": "Головна >> Гарантії"}
    return render(request, 'pages/guarantee.html', context=data)


def apartment(request):
    data = {"header_h1": "Квартири",
            "header_p": "Головна >> Квартири"}
    return render(request, 'pages/apartment.html', context=data)


def discounts(request):
    data = {"header_h1": "Знижки",
            "header_p": "Головна >> Знижки"}
    return render(request, 'pages/discounts.html', context=data)


def contact_us(request):
    data = {"header_h1": "Контакти",
            "header_p": "Головна >> Контакти"}
    return render(request, 'pages/contact_us.html', context=data)


def testimonials(request):
    data = {"header_h1": "Відгуки",
            "header_p": "Головна >> Відгуки"}
    return render(request, 'pages/testimonials.html', context=data)

def we_offer(request):
    data = {"header_h1": "ЩО <span>ПРОПОНУЄМО</span>",
            "header_p": "Головна >> Що пропонуємо"}
    return render(request, 'pages/we_offer.html', context=data)

  
def order(request):
    data = {"header_h1": "Замовити",
            "header_p": "Головна >> Замовити"}
    return render(request, 'pages/order.html', context=data)


def prices(request):
    data = {"header_h1": "Ціни",
            "header_p": "Головна >> Ціни"}
    return render(request, 'pages/prices.html', context=data)