from django.db import models

# Create your models here.
class BangTuongTacProduct(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to="static/images")