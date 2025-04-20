from rest_framework import serializers
from django.contrib.auth.models import User
from myapp.models import Forum, Comment, Book, Article
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    forum = serializers.PrimaryKeyRelatedField(queryset=Forum.objects.all())

    class Meta:
        model = Comment
        fields = ['id', 'forum', 'user', 'content', 'created_at', 'updated_at']

class ForumSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Forum
        fields = ['id', 'title', 'description', 'created_by', 'created_at', 'updated_at', 'comments']

class BookSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'published_date', 'created_by', 'created_at']

class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at']