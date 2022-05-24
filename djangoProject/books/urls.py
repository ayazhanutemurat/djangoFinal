from django.urls import path

from books.views import BookView, JournalView

urlpatterns = [
    path('books/', BookView.as_view({'get': 'list', 'post': 'create'})),
    path('books/<int:pk>/', BookView.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'})),
    path('journal/', JournalView.as_view({'get': 'list', 'post': 'create'})),
    path('journal/<int:pk>/', JournalView.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'})),

]