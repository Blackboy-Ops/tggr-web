from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from ckeditor.fields import RichTextField

class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
        ARCHIVED = 'AR', 'Archived'
    title = models.CharField(max_length=200)
    summary = models.TextField(blank=True, null=True)  # Short summary for previews
    content = RichTextField()  # Rich text field for the main content
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    slug = models.SlugField(unique=True, max_length=200,verbose_name="URL name of the page")  # For SEO-friendly URLs
    published_date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Add ImageField for post images
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True, verbose_name="Tags separated by comma")  # Comma-separated tags
     # Additional fields to improve user engagement
    view_count = models.PositiveIntegerField(default=0)  # Track how many times an article was viewed
    is_featured = models.BooleanField(default=False)  # Flag for featured articles

    class Meta:
        ordering = ['-published_date']  # Latest news first
        verbose_name_plural ='Posts'
        indexes = [
            models.Index(fields=['-published_date']),  # Index for faster queries
        ]

    def __str__(self):
        return self.title

    def increment_view_count(self):
        """Method to increment the view count each time the article is viewed."""
        self.view_count += 1
        self.save()

    def get_tags_list(self):
        """Returns tags as a list of strings."""
        return [tag.strip() for tag in self.tags.split(',')] if self.tags else []

    def __str__(self):
        return self.title