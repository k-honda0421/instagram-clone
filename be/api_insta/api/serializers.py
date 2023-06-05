from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Profile, Post, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        """
        オプションを記載
        models: userモデル
            シリアライザーの元になるmodelを定義
            get_user_modelはactiveなユーザーを取得(django組み込み)
        fields:
            シリアライザーで扱いたいparamを記述
        extra_kwargs:
            属性を指定
            passwordはclientから見られないようにwrite_only
        """
        model = get_user_model()
        # APIのレスポンスのkeyとなる
        fields = ("id", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """
        validated_dataで渡されたvalidate済のユーザーデータを使って
        ユーザーを作成する
        objectsはmodelに定義したUserManagerクラスで
        create_userはUserManagerクラスのメソッド

        Parameters
        ----------
        validated_data: dict
            validate済みのユーザーデータ

        Returns
        -------
        User
        """
        user = get_user_model().objects.create_user(**validated_data)
        return user


class ProfileSerializer(serializers.ModelSerializer):
    created_on = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = Profile
        fields = ("id", "nickName", "userProfile", "created_on", "img")
        extra_kwargs = {"userProfile": {"read_only": True}}


class PostSerializer(serializers.ModelSerializer):
    created_on = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = Post
        fields = ("id", "title", "userPost", "created_on", "img", "liked")
        extra_kwargs = {"userPost": {"read_only": True}}


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "text", "userComment", "post")
        extra_kwargs = {"userComment": {"read_only": True}}
