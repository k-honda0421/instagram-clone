from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from . import serializers
from .models import Profile, Post, Comment


class CreateUserView(generics.CreateAPIView):
    """
    user新規作成
    JWTで認証がなくてもユーザーの作成ができるよう
    permission_classes = (AllowAny,)を実装
    """
    serializer_class = serializers.UserSerializer
    permission_classes = (AllowAny,)


class ProfileViewSet(viewsets.ModelViewSet):
    """
    更新 + 新規作成をするためviewsets.ModelViewSetを継承
    """

    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    # jwt認証必須パラメータ
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        """
        overrideしている
        """
        serializer.save(userProfile=self.request.user)


class MyProfileListView(generics.ListAPIView):
    """
    ログインしているprofileを返す
    """

    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    # jwt認証必須パラメータ
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(userProfile=self.request.user)


class PostViewSet(viewsets.ModelViewSet):
    """
    更新 + 新規作成をするためviewsets.ModelViewSetを継承
    """

    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    # jwt認証必須パラメータ
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        """
        overrideしている
        """
        serializer.save(userPost=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    更新 + 新規作成をするためviewsets.ModelViewSetを継承
    """
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    # jwt認証必須パラメータ
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        """
        overrideしている
        """
        serializer.save(userComment=self.request.user)
