from django.contrib.auth.models import Permission, User
from django.db import models



class Profile(models.Model):
    user = models.ForeignKey(User, default=1)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField()

    def __str__(self):
        return self.user.username


