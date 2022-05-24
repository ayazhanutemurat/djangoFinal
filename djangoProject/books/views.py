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
    permission_classes = (AdminPermission,)

    def list(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def create(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            return Response({'success': True})
        except Book.DoesNotExist as e:
            return Response({"error": str(e)})

    def update(self, request, pk=None):
        instance = Book.objects.get(pk=pk)
        serializer = BookSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class JournalView(viewsets.ViewSet):
    permission_classes = (AdminPermission,)

    def list(self, request):
        journals = Journal.objects.all()
        serializer = JournalSerializer(journals, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Journal.objects.all()
        journal = get_object_or_404(queryset, pk=pk)
        serializer = JournalSerializer(journal)
        return Response(serializer.data)

    def create(self, request):
        serializer = JournalSerializer(data=request.data)
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

    def update(self, request, pk=None):
        instance = Journal.objects.get(pk=pk)
        serializer = JournalSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


