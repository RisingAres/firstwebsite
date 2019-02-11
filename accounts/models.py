from django.db import models
from django.conf import settings


class UserAccount(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.SET_NULL,
                                null=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.user.username
