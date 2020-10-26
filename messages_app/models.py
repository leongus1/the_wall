from django.db import models
from log_and_reg_app.models import Users

# Create your models here.
class Messages(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Users, related_name="messages",on_delete=models.CASCADE)
    

class Comments(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Users, related_name="comments", on_delete=models.CASCADE)
    message = models.ForeignKey(Messages, related_name="comments", on_delete=models.CASCADE)
