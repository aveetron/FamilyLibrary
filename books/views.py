from django.shortcuts import render
from books.models import * 
# Create your views here.
def home(request):
    allBook = Book.objects.all()
    context = {
        'allBook': allBook
    }
    return render(request, 'index.html', context)