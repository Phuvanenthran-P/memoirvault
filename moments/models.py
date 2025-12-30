from django.db import models
from django.contrib.auth.models import User

class Moment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    media = models.FileField(upload_to="moments/", blank=True, null=True)
    special_date = models.DateField(blank=True, null=True)
    remind_me = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
