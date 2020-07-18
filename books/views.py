from django.shortcuts import render
from books.models import * 
# Create your views here.
def home(request):
    allBook = Book.objects.all().order_by('-pk')
    context = {
        'allBook': allBook
    }
    return render(request, 'index.html', context)