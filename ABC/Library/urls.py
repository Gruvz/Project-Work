from django.contrib import admin
from django.urls import path,include
from .views import base, AddBook, ArticleDetailView

urlpatterns = [
    path('', base, name='base'),
    #path('', base.as_view(), name="base"),
    path('add_post/', AddBook.as_view(), name='add_post'),
    #path('add_post/', AddBook, name='add_post'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail')
]