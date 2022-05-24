from django.shortcuts import render
import json

# Create your views here.

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from books.models import Book, Journal
from books.serializer import BookSerializer, JournalSerializer
from books.permissions import AdminPermission


class BookView(viewsets.ViewSet):
    def get_permissions(self):
        permission_classes = (AdminPermission)
        return permission_classes

    def list(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def create(self, request, pk):
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(book)
        if serializer.is_valid():
            serializer.save()
            # book.add(book)
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            return Response({'success': True})
        except Book.DoesNotExist as e:
            return Response({"error": str(e)})


class JournalView(viewsets.ViewSet):
    def get_permissions(self):
        permission_classes = (AdminPermission)
        return permission_classes

    def list(self, request):
        journals = Journal.objects.all()
        serializer = JournalSerializer(journals, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Journal.objects.all()
        journal = get_object_or_404(queryset, pk=pk)
        serializer = JournalSerializer(journal)
        return Response(serializer.data)

    def create(self, request, pk):
        journal = Journal.objects.get(id=pk)
        serializer = JournalSerializer(journal)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk):
        try:
            journal = Journal.objects.get(id=pk)
            journal.delete()
            return Response({'success': True})
        except Journal.DoesNotExist as e:
            return Response({"error": str(e)})



