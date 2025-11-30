from django.shortcuts import render
from .models import User,Rating
# Create your views here.
def home(response):
    return render(response,'addis/home.html')
def portifolo(response):
    customers=User.objects.all()
    return render(response,'addis/portifolo.html',{"customers":customers})
def services(response):
    return render(response,'addis/services.html')
def contact(response):
    return render(response,'addis/contact.html')
def about(response):
    return render(response,'addis/about.html')
def privacy_and_policy(response):
    return render(response,'addis/p&p.html')
def terms_of_services(response):
    return render(response,'addis/terms.html')
def testimonial(response):
    return render(response,'addis/testimonial.html')
def pages(response):
    return render(response,'addis/pages.html')
def teams(response):
    return render(response,'addis/teams.html')
def order(response):
    return render(response,'addis/order.html')
def portifolo_detail(response,id):
    customer=User.objects.get(pk=id)
    return render(response,'addis/portifolo_detail.html',{"customer":customer})