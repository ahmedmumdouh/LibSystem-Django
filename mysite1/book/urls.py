from django.urls import path

from . import views
from .views import SearchResultsView

app_name='book'


urlpatterns = [
    
    path('book/', views.all_books , name='all_books'),
    path('book/<int:pk>/', views.book_detail , name='book_detail'),
    path('book/book_create', views.book_create , name='book_create'),
    path('book/edit/<int:pk>/', views.book_edit, name='book_edit'),
    path('book/delete/<int:pk>/', views.book_delete, name='book_delete'),
    path('', SearchResultsView.as_view(), name='search_results'),
    
]

