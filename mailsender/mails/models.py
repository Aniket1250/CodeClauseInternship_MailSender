from django.db import models

# Create your models here.
class Mail(models.Model):
    receipant = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)

    def __str__(self):
        return self.receipant