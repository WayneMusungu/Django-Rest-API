from django.urls import path
from . import views


urlpatterns = [
    path('', views.bookList),
    path('create-book/', views.createBook),
    path('detail-book/<int:id>/', views.detailBook),
    path('update-book/<int:id>/', views.updateBook),
    path('delete-book/<int:id>/', views.deleteBook),
    
]