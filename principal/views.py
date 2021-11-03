from django.shortcuts import render
from djangogit.http import HttpResponse

# Create your views here.
def index (request):
    return render(request,"principal/index.html")
