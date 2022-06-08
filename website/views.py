from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})


def blog(request):
    return render(request, 'blog.html', {})


def blogs(request):
    return render(request, 'blog-details.html', {})


def gallery(request):
    return render(request, 'gallery.html', {})


def menu(request):
    return render(request, 'menu.html', {})


def reservation(request):
    return render(request, 'reservation.html', {})


def stuff(request):
    return render(request, 'stuff.html', {})
