from django.urls import path , include

from . import views
#from .views import SearchResultsView

from rest_framework import routers

r_author = routers.DefaultRouter()
r_author.register('',views.author_list2)

r_user = routers.DefaultRouter()
r_user.register('',views.user_list)

app_name='author'


urlpatterns = [
    path('author/', views.all_authors , name='all_authors'),
    path('authors/', views.AuthorsList.as_view() , name='authors'),

    path('author/<int:pk>/', views.author_detail , name='author_detail'),
    path('author/author_create/', views.author_create , name='author_create'),
    path('author/edit/<int:pk>/', views.author_edit, name='author_edit'),
    path('author/delete/<int:pk>/', views.author_delete, name='author_delete'),
    path('author/api/', views.author_list.as_view()),
    path('author/apis/', include(r_author.urls)),
    path('user/apis/', include(r_user.urls)),

    
]

