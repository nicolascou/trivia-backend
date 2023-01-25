from django.db import models

class Winner(models.Model):
    name = models.CharField(max_length=20)
    points = models.IntegerField()

    def save(self, *args, **kwargs):
        if self.points < 5:
            return
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name