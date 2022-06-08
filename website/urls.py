from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='Home'),
    path('contact.html', views.contact, name="contact"),
    path('about.html', views.about, name="about"),
    path('blog.html', views.blog, name="blog"),
    path('blog-details.html', views.blogs, name="blogs"),
    path('gallery.html', views.gallery, name="contact"),
    path('menu.html', views.menu, name="menu"),
    path('reservation.html', views.reservation, name="reservation"),
    path('stuff.html', views.stuff, name="stuff"),

]
