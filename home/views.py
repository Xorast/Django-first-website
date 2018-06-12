from django.shortcuts import render
from .models import Book, Author

# Create your views here.
def get_index(request):
    
    book_items  = Book.objects.all()
    authors     = Author.objects.all()
    
    return render(request, "home/index.html", {'books' : book_items,'authors' : authors} )