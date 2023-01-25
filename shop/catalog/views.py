from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Book, Author

class CatalogView(TemplateView):
    template_name = "catalog/catalog.html"

    def get(self, request):
        books = Book.objects.all()

        params = {
            'books': books
        }

        return render(request, self.template_name, params)

class AuthorView(TemplateView):
    template_name = ""