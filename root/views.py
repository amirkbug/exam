from django.shortcuts import render
from .models import *
from django.http import HttpResponse


def Home(request):
    services = Services.objects.filter(status = True)
    specialservices = SpecialServices.objects.filter(status=True)
    questions = Questions.objects.all()
    prices = Pricing.objects.filter(status=True)
    makers = Makers.objects.filter(status=True)
    context = {
        "makers":makers,
        "prices":prices,
        "services" : services,
        "specialservices" : specialservices,
        "questions":questions,
    }
    return render(request,"root/index.html", context=context)

