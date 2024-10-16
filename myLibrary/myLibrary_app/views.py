from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render,redirect

from .models import reader,book
# Create your views here.

def home(request):
    return render(request,"home.html",context={'current_tab' : "home"})

def mybag(request):
    return render(request,"mybag.html",context={'current_tab' : "mybag"})

def returns(request):
    return render(request,"return.html",context={'current_tab' : "return"})

def shopping(request):
    return render(request,"shop.html",context={})

def save_stud(request):
    stud_name=request.POST['stud_name']
    stud_age=request.POST['stud_age']
    return render(request,"welcome_reader.html",context={'stud_name': stud_name})

def books(request):
    if 'search' in request.POST:
        searchitem=request.POST['search']
        books =book.objects.filter(book_name__icontains=searchitem).order_by('book_name')
    else:
        books =book.objects.all().order_by('book_name')
    return render(request,"books.html",context={'current_tab' : "books",'books': books})

def readers(request):
    if 'search' in request.POST:
        searchitem=request.POST['search']
        readers =reader.objects.filter(reference_id__icontains=searchitem)
    else:
        readers =reader.objects.all().order_by('reference_id')
    return render(request,"readers.html",context={'current_tab' : "readers",'readers':readers})

def save_reader(request):
    reader_item=reader(reference_id=request.POST['reference_id'],
                       reader_name=request.POST['reader_name'],
                       reader_contact=request.POST['reader_contact'],
                       reader_address=request.POST['reader_address'],
                       active=True)
    reader_item.save()
    return redirect('/readers')

def delete_reader(request):
    id=request.POST['reader_id']
    delete_item=reader.objects.get(id=id)
    delete_item.delete()
    return redirect('/readers')

def save_book(request):
    book_item=book(isbn_number=request.POST['isbn_number'],
                    book_name=request.POST['book_name'],
                    book_author=request.POST['book_author'],
                    book_price=request.POST['book_price'],
                    book_quntity=request.POST['book_quntity'])
    book_item.save()
    return redirect('/books')

def delete_book(request):
    id=request.POST['book_id']
    delete_item=book.objects.get(id=id)
    delete_item.delete()
    return redirect('/books')