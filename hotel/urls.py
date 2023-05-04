from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', views.home_page, name="home"),
    path('about/', views.about_page, name="about"),
    path('accomodation/', views.accomodation_page, name="accomodation"),
    path('blog/', views.blog_page, name="blog"),
    path('<int:pk>/', views.blog_single_page, name="blog-single"),
    path('contact/', views.contact_page, name="contact"),
    path('elements/', views.element_page, name="elements"),
    path('gallery/', views.gallery_page, name="gallery"),
    path("aba/", LoginView.as_view(template_name="aba.html"), name="aba")
]