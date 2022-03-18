from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from pyparsing import Or

from .models import User, Book, Order
from .forms import NewBookForm, NewAuthorForm

def index(request):
    return render(request, "Store/index.html", {
        "books" : Book.objects.all()
    })

def login_view(request):
    if request.method == 'POST':

        # Attempt to sign user in
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        # Check if authentication succesful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'Store/login.html', {
                'message': 'Неправильно введенные данные.'
            })
    else: 
        return render(request, 'Store/login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    pass

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "Store/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "Store/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "Store/register.html")

@login_required
def newBook(request):
    if request.method == "POST":
        form = NewBookForm(request.POST)
    

        if form.is_valid():
            # form.instance.Author = request.user
            form.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "Store/newBook.html", {
           "form" : form,
           "errors" : form.errors
              })
    form = NewBookForm()
    return render(request, "Store/newBook.html", {
            "form" : form
        })


@login_required
def newAuthor(request):
    if request.method == "POST":
        form = NewAuthorForm(request.POST)

        if form.is_valid():
            # form.instance.Author = request.user
            form.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "Store/newAuthor.html", {
                "form" : form
            })
    form = NewAuthorForm()
    return render(request, "Store/newAuthor.html", {
            "form" : form
        })


def book(request, book_id):
    book = Book.objects.get(pk=book_id)
   
    #inList = book.inShoplist(request.user) if request.user.is_authenticated else False
    try:
        Order.objects.get(Book=book)
        inList = True
    except Order.DoesNotExist:
        inList = False

   

    return render(request, "Store/book.html", {
            "book" : book,
            "inList" : inList 
        })

def shoplist(request):
    goods =  Order.objects.filter(Customer=request.user)
    if goods:
        mes = "message"
    else:
        mes = "no mes"
    return render(request, "Store/shoplist.html",
    {
        "goods":goods,
        "mes": mes
    })

def shoplistChange(request, book_id):
    book = Book.objects.get(pk=book_id)
    user = request.user
    order = Order(Customer = user, Book=book)
    order.save()
    return render(request, "Store/index.html")
    

    