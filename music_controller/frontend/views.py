from django.shortcuts import render

# Create your views here.
# here we will render the 

def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html')