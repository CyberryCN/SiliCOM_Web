from django.shortcuts import render, get_object_or_404
from .models import Level, Book

# Create your views here.
def level_list(request):
    levels = Level.objects.all().order_by('level_id')
    return render(request, 'suggestion/level_list.html', {
        'levels': levels
    })

def book_list(request, level_id):
    level = get_object_or_404(Level, level_id=level_id)
    books = level.books.all()
    return render(request, 'suggestion/book_list.html', {
        'level': level,
        'books': books
    })

def book_detail(request, level_id, book_label):
    book = get_object_or_404(
        Book,
        level__level_id=level_id,
        book_label=book_label
    )
    return render(request, 'suggestion/book_detail.html', {
        'book': book
    })