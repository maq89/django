import string
from django.http import HttpResponse
from django.views import generic
from .models import Category, Author, Book


class IndexView(generic.ListView):

    template_name = 'index.html'
    context_object_name = 'books'
    paginate_by = 1

    def get_queryset(self):
        return Book.objects.all().values('book_id', 'book_title', 'book_cover', 'book_description')


class DetailView(generic.DetailView):

    model = Book
    template_name = 'detail.html'


def pdf_download(request, book_id):
    book = Book.objects.get(pk=book_id)
    book_name = book.book_title.replace(' ', '_')
    response = HttpResponse(book.book_pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename='+book_name+'.pdf'
    return response



