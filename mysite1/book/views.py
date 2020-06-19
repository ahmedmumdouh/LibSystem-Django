from django.shortcuts import render , get_object_or_404 , redirect
#from django.utils import timezone
from django.db.models import Q
from .models import Book
from .forms import BookForm
from django.views.generic import ListView
# Create your views here.


# ##################### library Views ##################

# # def library (request):
# #     all_books = Book.objects.all()
# #     all_authors = Author.objects.all()
# #     return render(request,'library.html' , context)

class SearchResultsView(ListView):
    model = Book 
    template_name = 'library.html'
    #queryset = Author.objects.filter(full_name='ahmed')
    # object_list = Author.objects.all()

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        if ( not query):
            object_list = Book.objects.all()
        else :
            object_list = Book.objects.filter( Q(author__full_name=query) | Q(title=query) )
        #object_lists = Book.objects.filter( Q(title=query) )
        return object_list 

    


# ######################## books Views #######################


def all_books(request):
    all_books = Book.objects.all()
    context ={
        'all_books' : all_books ,
    }
    return render(request,'book/all_books.html' , context)

def book_detail (request,pk):
    book = get_object_or_404(Book , id=pk)
    #author = Author.objects.get(id=book.author)
    context ={
        'book' : book ,
    }
    return render(request,'book/book_detail.html' , context)


def book_edit (request,pk):
    book = get_object_or_404(Book , id=pk)
    if request.method == 'POST':
        form = BookForm(request.POST , instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            # post.user = request.user
            # post.published_date = timezone.now()
            book.save()
            return redirect('/book')
    else :
        form = BookForm(instance=book)

    context = {
        'form' : form ,
    }
    return render(request,'book/book_edit.html' , context)

def book_delete (request,pk):
    book = get_object_or_404(Book , id=pk)
    # post.delete()
    # return redirect('/blog')
    if request.method == 'POST':  
        #post.user = request.user
        #post.published_date = timezone.now()  
        book.delete()
        return redirect('/book')    
   
    else :
        form = BookForm()

    context = {
        'form' : form ,
        'book' : book ,
    }
    return render(request,'book/book_delete.html' , context)


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            # post.user = request.user
            # post.published_date = timezone.now()
            book.save()
            return redirect('/book')
    else :
        form =BookForm()

    context = {
        'form' : form ,
    }
    return render(request,'book/book_create.html', context)