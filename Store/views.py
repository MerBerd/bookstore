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
            form.instance.Poster = request.user
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
    user = request.user
    sth = user == book.Poster
    Authors = book.Author.all()
    info = ''
    for aut in Authors:
        info += f' {aut} ' 

   
    #inList = book.inShoplist(request.user) if request.user.is_authenticated else False
    try:
        Order.objects.get(Book=book)
        inList = True
    except Order.DoesNotExist:
        inList = False

   

    return render(request, "Store/book.html", {
            "book" : book,
            "inList" : inList,
            "info" : info,
            "sth" : sth
        })

def shoplist(request):
    goods =  Order.objects.filter(Customer=request.user)
    cost = 0
    for good in goods:
        cost += good.Book.Price
    if goods:
        mes = "message"
    else:
        mes = "no mes"
    return render(request, "Store/shoplist.html",
    {
        "goods":goods,
        "mes": mes,
        "cost" : cost
    })

def shoplistChange(request, book_id):
    _book = Book.objects.get(pk=book_id)
    user = request.user
    order = Order(Customer = user, Book=_book)
    order.save()

    try:
        Order.objects.get(Book=_book)
        inList = True
    except Order.DoesNotExist:
        inList = False

    return render(request, "Store/book.html", {
            "book" : _book,
            "inList" : inList 
        })
    
    

def shoplistRemove(request, book_id):
    
    user = request.user
    book = Book.objects.get(pk=book_id)

    Order.objects.filter(Customer=user, Book=book).delete()
    return HttpResponseRedirect(reverse("shoplist"))

def edit(request, book_id):
    book = Book.objects.get(pk=book_id)
    if request.method == "POST":
        form = NewBookForm(request.POST)
        

        if form.is_valid():
            book.Title = form.cleaned_data["Title"]
            book.Description = form.cleaned_data["Description"]
            book.Price = form.cleaned_data["Price"]
            book.Photo = form.cleaned_data["Photo"]
            book.Author.set(form.cleaned_data["Author"])
            book.save()

            
            
            return HttpResponseRedirect(reverse("index"))
    
    
    initial_ = {
    "Title": book.Title,
    "Description" : book.Description,
    "Price" : book.Price,
    "Photo" : book.Photo,
    
    }
    
    form = NewBookForm(request.POST or None, initial=initial_)
    
    return render(request, "Store/edit.html",
    {
        "form" : form,
        "book" : book
        
    })
            

def delete(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()
    return HttpResponseRedirect(reverse("index"))
    

    