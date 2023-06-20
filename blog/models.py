from django.db import models
from user_mgt.models import User

class BlogPost(models.Model):
    BLOG_CATEGORIES = (
        ('Mental Health', 'Mental Health'),
        ('Heart Disease', 'Heart Disease'),
        ('Covid19', 'Covid 19'),
        ('Immunization', 'Immunization')
    )
    category = models.CharField(max_length=30, choices=BLOG_CATEGORIES)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images')
    summary = models.CharField(max_length=200)
    content = models.TextField()
    is_draft = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title