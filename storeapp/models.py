from django.db import models

# Create your models here.


class Product(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=150)
    color = models.CharField(max_length=50)
    description = models.TextField()
    category = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    rating = models.CharField(max_length=5, blank=True, null=True)
    slug = models.SlugField(unique=True, null=False, blank=False)
    like = models.PositiveIntegerField(blank=True, null=True)
    disponible_date = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=3, max_digits=6, default=0.0)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
