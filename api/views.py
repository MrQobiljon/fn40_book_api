from rest_framework.viewsets import ModelViewSet

from .models import Author, Book, Publisher
from .serializers import AuthorSerializer, BookSerializer, AuthorSerializerForDetail, PublisherSerializer



class AuthorApiViewSet(ModelViewSet):
    queryset = Author.objects.all().prefetch_related('book_set')
    serializer_class = AuthorSerializer

    def get_serializer_class(self):
        if self.kwargs.get('pk'):
            return AuthorSerializerForDetail
        return self.serializer_class


class BookApiViewSet(ModelViewSet):
    # queryset = Book.objects.all().select_related('publisher').prefetch_related('author').only('id', 'title', 'price', 'published_year', 'author', 'publisher')
    queryset = Book.objects.all().select_related('publisher').prefetch_related('author').defer('text')
    serializer_class = BookSerializer


class PublisherApiViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer