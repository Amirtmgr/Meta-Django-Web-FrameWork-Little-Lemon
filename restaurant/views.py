# from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Menu
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            # Add the success message here
            messages.success(request, "Thank you for booking. Your booking will be handled promptly.")
            return redirect('book') # Redirect to clear the form
    context = {'form':form}
    return render(request, 'book.html', context)

# Add your code here to create new views
def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu":menu_data}
    return render(request, 'menu.html', main_data)

def display_menu_item(request, pk = None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ''
    return render(request, "menu_item.html", {"menu_item" : menu_item})     