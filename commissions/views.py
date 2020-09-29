from django.shortcuts import render
from django.http import HttpResponse
from .models import Commission

# Create your views here.
def home(request):
    # when you render an html page to be shown to the user, you can pass forward some information in a dictionary
    return render(request, 'home.html', {'commissions': Commission.objects.all()})