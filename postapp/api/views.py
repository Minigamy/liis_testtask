from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoObjectPermissions

from users.models import CustomUser
from .permissions import IsSubOrAuthor
from ..models import Post
from .serializers import PostSerializer
from . import serializers


class PostListView(generics.ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        if self.request.user.groups.filter(name__in=['Author', 'Subscriber']).exists() or self.request.user.is_staff:
            return Post.objects.all()
        else:
            return Post.objects.filter(private=False)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsSubOrAuthor, )


class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
