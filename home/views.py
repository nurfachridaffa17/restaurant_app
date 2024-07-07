from django.shortcuts import render
from meals.models import Meals, Category
from contact.models import Contact
from aboutus.models import AboutUs, WhyChooseUs
from blog.models import Post

# Create your views here.
def home(request):
    post_list = Post.objects.all()
    aboutus = AboutUs.objects.last()
    whychooseus = WhyChooseUs.objects.all()
    contact = Contact.objects.all()
    menu = Meals.objects.all()
    categories = Category.objects.all()


    context = {
        'post_list' : post_list,
        'aboutus' : aboutus,
        'whychooseus' : whychooseus,
        'contact' : contact,
        'menu' : menu,
        'categories' : categories
    }

    return render(request, 'home/index.html', context)