from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from apartments.models import Apartments
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'User logged in')
            messages.error(request, 'error test')
            messages.warning(request, 'warning test')

            return redirect('dashboard')
        else:
            messages.error(request, 'Incorrect login or password')
            return redirect('login')
    #request.method == GET
    data = {"header_h1": "Вхід",
            "header_p": "Головна >> Вхід"}
    return render(request, 'account/login.html', context=data)


def register(request):
    if request.method == 'POST':
        first_name = request.POST['Name']
        last_name = request.POST['Surname']
        username = request.POST['Username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        user_condition = not User.objects.filter(username=username).exists()
        password_condition = password == confirm_password
        email_condition = not User.objects.filter(email=email).exists()

        if user_condition and password_condition and email_condition:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name,
            )
            user.save()
            messages.success(request, 'User registered')
            return redirect('login')
        else:
            if not user_condition:
                messages.error(request, "User with login '" +
                               username + "' exists")
            if not password_condition:
                messages.error(request, "Passwords do not match")
            if not email_condition:
                messages.error(request, "User with email '"+email+"' exists")
            return redirect("register")
    #request.method == GET
    data = {"header_h1": "Реєстрація",
            "header_p": "Головна >> Реєстрація"}
    return render(request, 'account/register.html', context=data)


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "Logged out")
    return redirect('index')


@login_required
def dashboard(request):
    apartments = Apartments.objects.order_by(
        '-list_date').filter(is_published=True, favorits=request.user)

    paginator = Paginator(apartments, 2)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        "apartments": page,
        "header_h1": "Dashboard",
        "header_p": "Головна >> Dashboard",
    }

    return render(request, 'account/dashboard.html', context)
