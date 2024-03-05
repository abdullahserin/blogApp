from rest_framework import serializers
from .models import Blog, Category, Comment, Likes, PostViews

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    total_comments = serializers.SerializerMethodField()
    total_likes = serializers.SerializerMethodField()
    total_views = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = '__all__'

    def get_total_comments(self, obj):
        return obj.comments.count()

    def get_total_likes(self, obj):
        return obj.likes.all().count()

    def get_total_views(self, obj):
        return obj.views.count()


class UserBlogSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Blog
        exclude = ('status',)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = '__all__'

class PostViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostViews
        fields = '__all__'


