from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)


class CommentSerializer(serializers.ModelSerializer):
    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title', )
    article = ArticleTitleSerializer(read_only = True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article', )

class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many = True, read_only = True)
    comment_count = serializers.IntegerField(source = 'comment_set.count', read_only = True)

    class Meta:
        model = Article
        fields = '__all__'
    
    # 특정 필드를 override 혹은 추가한 경우 동작하지 않는다.
    # read_only_fields = ('comment_set', 'comment_count', )
