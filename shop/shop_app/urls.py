from django.urls import path

from . import views

urlpatterns = [
    path('', views.startpage, name='startpage'),
    path('books/', views.BookListView.as_view(), name='books_list'),
    path('books/detail/<int:pk>', views.book_detail, name='book_detail'),
]
