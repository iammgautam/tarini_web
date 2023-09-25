from django.shortcuts import render
from twilio.rest import Client
import os
# Create your views here.
def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def sms_sent(request):
    account_sid = 'ACb4812c29ad3ed5f0f563d82ce8045ab8'
    auth_token = '537ab06fade696e6dd8e615abbe00f48'
    client = Client(account_sid, auth_token)

    full_name = request.GET.get("full_name")
    phone_number = request.GET.get("phone_number")
    pet = request.GET.get("pet_breed")
    reason = request.GET.get("message")
    body = (
        "Booking From Website: "
        + "\nName: "
        + full_name
        + "\nPhone Number: "
        + phone_number
        + "\nPet Breed: "
        + pet
        + "\nReason: "
        + reason
    )
    message = client.messages.create(
        body=body, from_="+18509983979", to="+919365027852"
    )
    return render(request, "contact.html")