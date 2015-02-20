from django.db import models


class Stat(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    up = models.BigIntegerField()
    down = models.BigIntegerField()
    live_time = models.BigIntegerField()
