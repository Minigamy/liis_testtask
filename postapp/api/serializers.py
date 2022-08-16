from rest_framework import serializers

from users.models import CustomUser
from ..models import Post


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'date_joined')


class PostSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer(many=False, read_only=True)
    user = serializers.ReadOnlyField(source='author.email')
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ('id', 'user', 'title', 'text', 'private', 'created_date', 'published_date', 'author')


class UserSerializer(serializers.ModelSerializer):
    post_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'post_set']
