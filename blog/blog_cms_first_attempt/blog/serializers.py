from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'slug', 'created_at', 'updated_at', 'image', 'published_date', 'summary', 'view_count', 'is_featured', 'tags',]
        read_only_fields = ['created_at', 'updated_at', 'view_count']
    
    def get_tags(self, obj):
        return list(obj.tags.values_list('name', flat=True))