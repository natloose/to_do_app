from django.db import models


class ToBeDone(models.Model):
    to_do = models.CharField(max_length=200)

    def __str__(self):
        return self.to_do