from django.db import models
from log_and_reg_app.models import Users
import datetime
from datetime import datetime, timezone
# Create your models here.

class PostManager(models.Manager):
    def post_timely(self, message):
        time_diff = datetime.now(timezone.utc)-message.modified_at
        if time_diff.days > 0 or time_diff.seconds > 1800:
            return False
        else: 
            return True
        
class Messages(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Users, related_name="messages",on_delete=models.CASCADE)
    objects = PostManager()
    
    def timely(self):
        time_diff = datetime.now(timezone.utc)-self.modified_at
        if time_diff.days > 0 or time_diff.seconds > 1800:
            return False
        else: 
            return True
    

class Comments(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Users, related_name="comments", on_delete=models.CASCADE)
    message = models.ForeignKey(Messages, related_name="comments", on_delete=models.CASCADE)
    objects = PostManager()
    
    def timely(self):
        time_diff = datetime.now(timezone.utc)-self.modified_at
        if time_diff.days > 0 or time_diff.seconds > 1800:
            return False
        else: 
            return True
    
    

        
    
            
