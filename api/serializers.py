from rest_framework import serializers

from .models import Author, Book, Publisher



class BookSerializerForAuthor(serializers.ModelSerializer):
    class Meta:
        model = Book
        # fields = '__all__'
        exclude = ['author']


class AuthorSerializerForDetail(serializers.ModelSerializer):

    books = BookSerializerForAuthor(many=True, read_only=True, source="book_set")

    class Meta:
        model = Author
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    publisher_name = serializers.CharField(source="publisher.name")
    class Meta:
        model = Book
        # fields = '__all__'
        exclude = ['text']


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'