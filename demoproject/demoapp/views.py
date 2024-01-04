from django.shortcuts import render
from requests import request
from . models import Place

# Create your views here.

def index(request):
    object  = Place.objects.all()
    return render(request, 'index.html')






# def home(request):
#     return render(request,'home.html')

# def calculate(request):
#     x=(int(request.GET['num1']))
#     y=(int(request.GET['num2']))
#     add=x+y
#     sub=x-y
#     mul=x*y
#     div=x/y
#     return render(request,'calculate.html', {'add':add, 'sub':sub, 'mul':mul, 'div':div} )



# def about(request):
#     return render(request,'about.html')
# def contact(request):
#     return render(request,'contact.html')

# def details(request):
#     return render(request,'details.html')
# def thanks(request):
#     return render(request,'thanks.html')