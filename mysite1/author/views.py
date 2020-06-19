from django.shortcuts import render , get_object_or_404 , redirect
#from django.utils import timezone
from django.db.models import Q
from .models import Author #, Book
from  book.models import Book
from .forms import AuthorForm  #, BookForm

from rest_framework.response import Response

from .api_json import AuthorApi , UserApi
from rest_framework.views import APIView
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView ,DetailView
# Create your views here.

####### Api ################
class author_list(APIView):
    def get(self, request):
        author_model=Author.objects.all()
        author_api=AuthorApi(author_model,many=True)
        return Response(author_api.data)

    def post(self):
        pass

class author_list2(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorApi

class user_list(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserApi



########################

def all_authors(request):
    all_authors = Author.objects.all()
    context ={
        'all_authors' : all_authors ,
    }
    return render(request,'author/all_authors.html' , context)

class AuthorsList (ListView):
    template_name = 'author/authors_list.html'
    # context_object_name = all_authors
    queryset = Author.objects.all()

def author_detail (request,pk):
    author = get_object_or_404(Author , id=pk)
    list_books = Book.objects.filter(author=pk)
    context ={
        'p' : author ,
        'books' : list_books  ,
    }
    return render(request,'author/author_detail.html' , context)


def author_edit (request,pk):
    author = get_object_or_404(Author , id=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST , instance=author)
        if form.is_valid():
            author = form.save(commit=False)
            # post.user = request.user
            # post.published_date = timezone.now()
            author.save()
            return redirect('/author')
    else :
        form = AuthorForm(instance=author)

    context = {
        'form' : form ,
    }
    return render(request,'author/author_edit.html' , context)

def author_delete (request,pk):
    author = get_object_or_404(Author , id=pk)
    list_books = Book.objects.filter(author=pk)
    # post.delete()
    # return redirect('/blog')
    if request.method == 'POST':  
        #post.user = request.user
        #post.published_date = timezone.now()  
        author.delete()
        return redirect('/author')    
   
    else :
        form = AuthorForm()

    context = {
        'form' : form ,
        'p' : author ,
        'books' : list_books  ,

    }
    return render(request,'author/author_delete.html' , context)


def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            # post.user = request.user
            # post.published_date = timezone.now()
            author.save()
            return redirect('/author')
    else :
        form = AuthorForm()

    context = {
        'form' : form ,
    }
    return render(request,'author/author_create.html', context)

