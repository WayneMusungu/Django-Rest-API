from django.shortcuts import render
from django.http import JsonResponse
from .models import Books
from .seriaizers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



# Create your views here.

@api_view(['GET'])
def bookList(request):
    if request.method == 'GET':
        books = Books.objects.all()
        serializer = BookSerializer(books, many=True)
        return JsonResponse({"books":serializer.data})
    
@api_view(['POST'])
def createBook(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET'])
def detailBook(request, id):
    try:
        book = Books.objects.get(pk=id)
    except Books.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
@api_view(['PUT'])
def updateBook(request, id):
    try:
        book = Books.objects.get(pk=id)
    except Books.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = BookSerializer(instance=book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteBook(request, id):
    try:
        book = Books.objects.get(pk=id)
    except Books.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        book.delete()
    return Response('Book deleted successfully')




