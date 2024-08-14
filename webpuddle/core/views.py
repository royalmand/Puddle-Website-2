from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignUpForm


# Create your views here.
def index(request):
    """
    Handles the index view of the application, retrieving a list of unsold items and all categories.
    
    Parameters:
    request (HttpRequest): The current HTTP request object.
    
    Returns:
    HttpResponse: A rendered HTML response containing the index page with the retrieved items and categories.
    """
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items
    })

def about(request):
    return render(request, 'core/about.html')

def privacypolicy(request):
    return render(request, 'core/privacypolicy.html')

def tou(request):
    return render(request, 'core/tou.html')

def contact(request):
    """
    Handles the contact view of the application, retrieving the contact page.
    
    Parameters:
    request (HttpRequest): The current HTTP request object.
    
    Returns:
    HttpResponse: A rendered HTML response containing the contact page.
    """
    return render(request, 'core/contact.html')

# Untuk login, login view nya pakai default dari django
def signup(request):
    """
    Handles the signup view of the application, creating a new signup form and rendering the signup page.
    
    Parameters:
    request (HttpRequest): The current HTTP request object.
    
    Returns:
    HttpResponse: A rendered HTML response containing the signup page with the created form.
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignUpForm()

    form = SignUpForm()
    return render(request, 'core/signup.html', {
        'form':form
    })
