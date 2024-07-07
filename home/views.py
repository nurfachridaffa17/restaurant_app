from django.shortcuts import render

# Create your views here.
def home():
    context = {}
    return render('home/index.html', context)