from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    # user base model User, delete CASCADE, revert attr for model "profile"
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    # field for desc,
    description = models.TextField(blank=True, null=True)
    # exmpl city
    location = models.CharField(max_length=30, blank=True)
    # date of registy
    date_joined = models.DateTimeField(auto_now_add=True)
    # if object updated it takes date of this event
    updated_on = models.DateTimeField(auto_now=True)
    # flag, by default all user have flag simple user.
    simple_user = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
