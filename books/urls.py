from django.urls import path
from . import views
from books.views import BookDelete, BookDetail, BookList, BookCreate, BookUpdate


urlpatterns = [
    #FUNCTION BASED VIEWS PATH
    # path('', views.bookList),
    # path('create-book/', views.createBook),
    # path('detail-book/<int:id>/', views.detailBook),
    # path('update-book/<int:id>/', views.updateBook),
    # path('delete-book/<int:id>/', views.deleteBook),
    
    #CLASS BASED VIEWS PATH
    path('', BookList.as_view()),
    path('create-book/', BookCreate.as_view()),
    path('detail-book/<int:id>/', BookDetail.as_view()),
    path('update-book/<int:id>/', BookUpdate.as_view()),
     path('delete-book/<int:id>/', BookDelete.as_view()),
    
    
    
    
]