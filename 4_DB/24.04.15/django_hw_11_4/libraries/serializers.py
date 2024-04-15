from rest_framework import serializers
from .models import Book, Review


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', )

class BookSerializer(serializers.ModelSerializer):
    class ReviewBookSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('content', 'score',)
    review_set = ReviewBookSerializer(many = True, read_only = True)
    review_count = serializers.IntegerField(source = 'review_set.count', read_only = True)

    class Meta:
        model = Book
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"
        read_only_fields = ('created_at', 'updated_at', 'book')

class ReviewListSerializer(serializers.ModelSerializer):
    class BookReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Book
            fields = ('isbn', )
    book = BookReviewSerializer(read_only = True)

    class Meta:
        model = Review
        fields = ('book', 'content', 'score',)
        read_only_fields = ('book', )