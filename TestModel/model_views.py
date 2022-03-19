from django.shortcuts import render


# Create your views here.

def model_index(request):
    return render(request, "model_index.html")
