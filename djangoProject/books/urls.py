from django.urls import path

from books.views import BookView, JournalView

urlpatterns = [
    path('books/', BookView.as_view({'list', 'retrieve', 'destroy', 'create'})),
    path('journals/', JournalView.as_view({'list', 'retrieve', 'destroy', 'create'}))

]