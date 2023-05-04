from django.contrib import admin
from .models import Accomodation, Facility, Article, Testimony, Categories, Blog_Post, Gallery, Subscriber, Contact

# Register your models here.
admin.site.register([Accomodation, Facility, Article, Testimony, Categories, Blog_Post, Gallery, Subscriber, Contact]),