from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Task(models.Model):
    TITLE_MAX_LEN =20
    DESC_MAX_LEN =100

    title = models.CharField(max_length=TITLE_MAX_LEN)
    description = models.TextField(max_length=DESC_MAX_LEN)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
