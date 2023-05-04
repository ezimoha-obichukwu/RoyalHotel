from django.db import models

# Create your models here.
class Accomodation(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    button = models.CharField(max_length=20)
    image = models.ImageField(upload_to="accomodation_images")

    def __str__(self):
        return self.title
    
class Facility(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Facilities'

    def __str__(self):
        return self.title
    
class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="article_images")
    button = models.CharField(max_length=30)

    def __str__(self):
        return self.title
    

class Testimony(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="testimony_images")

    class Meta:
        verbose_name_plural = 'Testimonies'

    def __str__(self):
        return self.name
    
class Categories(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="category_images", blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class Blog_Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="blogpost_images")
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    user = models.CharField(max_length=100)
    viewers = models.CharField(max_length=50)
    commentry = models.CharField(max_length=1000)
    Button = models.CharField(max_length=100, default="View More")

    class Meta:
        verbose_name_plural = 'BlogPost'

    def __str__(self):
        return self.title
    
class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery_images")

    class Meta:
        verbose_name_plural = 'Galleries'

class Subscriber(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
    
class Contact(models.Model):
    SUBJECT_CHOICES = (
        ("Inquiry", "Inquiry"),
        ("Complaint", "Complaint")
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100, choices=SUBJECT_CHOICES)
    message = models.TextField()

    def __str__(self):
        return self.name
    

    





    