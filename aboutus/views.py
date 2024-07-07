from django.shortcuts import render
from .models import AboutUs, WhyChooseUs, Chef

# Create your views here.
def aboutus_list(request):
    aboutus = AboutUs.objects.last()
    whychooseus = WhyChooseUs.objects.all()
    chef = Chef.objects.all()
    context = {
        'aboutus' : aboutus,
        'whychooseus' : whychooseus,
        'chef' : chef
    }
    return render(request, 'About/about.html', context)