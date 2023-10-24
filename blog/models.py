from django.db import models
from accounts.models import CustomUser # new
import uuid


# Create your models here.
class Post(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title + " | " + str(self.author)
