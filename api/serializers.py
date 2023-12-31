from rest_framework import serializers
from api.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user', 'title', 'content')
        read_only_fields = ('id', 'user')
