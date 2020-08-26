from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Contact
from django.core.mail import send_mail
from django.contrib import messages


def contact(request):
    if request.method == "POST":
        apartment_id = request.POST['apartment_id']
        name = request.POST['name']
        apartment_title = request.POST['apartment_title']
        email = request.POST['email']
        realtor_email = request.POST['realtor_email'] or 'pet.pluta@gmail.com'
        phone = request.POST['phone']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id
            contact = Contact.objects.all().filter(
                apartment_id=apartment_id, user_id=user_id)
            if contact:
                messages.warning(request, "Contact was already added earlier!")
            else:
                contact = Contact(title=apartment_title, apartment_id=apartment_id,
                                  name=name, email=email, phone=phone, message=message, user_id=request.user.id)
                contact.save()
                try:
                    print("realtor_email",realtor_email)
                    send_mail(
                        "New connect",
                        "Apartment for " + apartment_title + "contact with new client",
                        "from",
                        [realtor_email, ],
                        fail_silently=False
                    )
                    messages.success(request, "Email was sent to realtor")
                except:
                    messages.error(request, "Email sending fail!")

        return redirect(reverse("apartment", kwargs={"apartment_id": apartment_id}))
