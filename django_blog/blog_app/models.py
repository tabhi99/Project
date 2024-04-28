from django.db import models
from django.conf import settings
from django.utils import timezone
class BlogPost(models.Model):
    Author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    Title=models.CharField(max_length=255)
    Blog_Content=models.TextField()
    Create_Date=models.DateTimeField(default=timezone.now)
    Publish_Date=models.DateTimeField(blank=True,null=True)
    def publish(self):
        self.Publish_Date=timezone.now()
        self.save()
    def __str__(self):
        return self.Title

# Create your models here.
