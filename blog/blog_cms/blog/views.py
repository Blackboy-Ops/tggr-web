from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow everyone to read, restrict write
    lookup_field = 'slug'  # Use slug instead of id for detail views


    def perform_create(self, serializer):
        """Customize the creation process by automatically setting the author."""
        serializer.save(author=self.request.user)  # Set the author to the currently logged-in user

    def get_queryset(self):
        queryset = super().get_queryset()
        tags = self.request.query_params.get('tags')
        if tags:
            tag_list = tags.split(',')
            queryset = queryset.filter(tags__name__in=tag_list).distinct()
        return queryset