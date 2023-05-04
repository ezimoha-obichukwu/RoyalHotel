from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Accomodation, Facility, Article, Testimony, Categories, Blog_Post, Gallery, Subscriber, Contact

# Create your views here.
def home_page(request):
    if request.method == "GET":
        accomodation = Accomodation.objects.all()
        facility = Facility.objects.all()
        article = Article.objects.all()
        testimony = Testimony.objects.all()
        latest_post = Blog_Post.objects.filter(category__name="Lifestyle")
        context = {
            "all_accomodation": accomodation,
            "all_facility": facility,
            "all_article": article,
            "all_testimonies": testimony,
            "all_latest_post": latest_post
        }
        return render(request, "index.html", context)
    elif request.method == "POST":
        newsletter = request.POST["email"]

        Subscriber.objects.create(email=newsletter)
        return redirect("home")

def about_page(request):
    if request.method == "GET":    
        facility = Facility.objects.all()
        testimony = Testimony.objects.all()
        article = Article.objects.all()
        context = {
            "all_facility": facility,
            "all_testimonies": testimony,
            "all_article": article,
        }
        return render(request, "about.html", context)
    elif request.method == "POST":
        newsletter = request.POST["email"]

        Subscriber.objects.create(email=newsletter)
        messages.success(request, f"Hello, {newsletter} Your submission was successful")
        # return HttpResponse("<h2>You Submittion was successful</h2>")
        return redirect("about")


def accomodation_page(request):
    if request.method == "GET":
        accomodation = Accomodation.objects.all()
        context = {
            "all_accomodation": accomodation,
        }
        return render(request, "accomodation.html", context)
    elif request.method == "POST":
        newsletter = request.POST["email"]
        
        Subscriber.objects.create(email=newsletter)
        messages.success(request, f"Hello, {newsletter} Your submission was successful")
        # return HttpResponse("<h2>You Submittion was successful</h2>")
        return redirect("home")


def blog_page(request):
    if request.method == "GET":
        category = Categories.objects.all()
        blog_post = Blog_Post.objects.filter()
        context = {
            "all_categories": category,
            "all_blog_post": blog_post,
        }
        return render(request, "blog.html", context)
    elif request.method == "POST":
        newsletter = request.POST["email"] # OR request.POST["email"]

        Subscriber.objects.create(email=newsletter)
        return redirect("home")

def blog_single_page(request, pk):
    if request.method == "GET":
        single_page = Blog_Post.objects.get(pk=pk)
        context = {
            "all_single_page": single_page
        }
        return render(request, "blog-single.html", context)
    elif request.method == "POST":
        contact = request.POST["email"] # OR request.POST["email"]

        Contact.objects.create(email=contact)
        return redirect("home")


def contact_page(request):
    if request.method =="GET":
        return render(request, "contact.html")
    elif request.method == "POST":
        new_contact_name = request.POST["name"]
        new_contact_email = request.POST["email"] # OR request.POST.get["email"]
        new_contact_subject = request.POST["subject"]
        new_contact_message = request.POST["message"]
        
        Contact.objects.create(name=new_contact_name, email=new_contact_email, subject =new_contact_subject, message=new_contact_message  )
        return redirect("home")
    elif request.method == "POST":
        newsletter = request.POST["email"]

        Subscriber.objects.create(email=newsletter)
        return redirect("home")


def element_page(request):
    return render(request, "elements.html")

def gallery_page(request):
    if request.method == "GET":
        gallery = Gallery.objects.all()
        context = {
            "all_galleries": gallery
        }
        return render(request, "gallery.html", context)
    elif request.method == "POST":
        newsletter = request.POST["email"]

        Subscriber.objects.create(email=newsletter)
        return redirect("home")

# def text(request):
#     if request.method == "GET":
#         return render(request, "aba.html")
#     elif request.method == "POST":
#         new_subscriber = request.POST["email"]

#         Subscriber.objects.create()
#         return redirect("home")
    
#     def __str__(self):
#         return self.email