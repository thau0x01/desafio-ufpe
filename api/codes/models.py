from django.db import models

class Code(models.Model):
    code = models.JSONField()

    class Meta:
        app_label = "codes"


class Safebox(models.Model):
    code = models.JSONField()

    class Meta:
        app_label = "codes"


class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=20)

    class Meta:
        app_label = "codes"
    

class SecretNote(models.Model):
    note = models.TextField(max_length=1024)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        app_label = "codes"

    def __str__(self) -> str:
        return self.note