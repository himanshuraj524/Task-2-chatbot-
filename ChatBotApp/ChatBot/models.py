from django.db import models

# Create your models here.
class UserMessage(models.Model):
    """
    This model is used to store the UserQuery along with the messageID and Time.
    """
    messsgeID = models.AutoField(primary_key=True)
    UserQuery = models.TextField()
    Time = models.DateTimeField(auto_now_add=True, blank=True)