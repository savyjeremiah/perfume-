from django.db import models


class Perfume(models.Model):
    name = models.CharField(max_length=200)
    size = models.CharField(max_length=100)  # Singular form for clarity
    group = models.CharField(max_length=100)  # Renamed for clarity
    image = models.ImageField(upload_to='perfume_images/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Better for currency

    def __str__(self):
        return self.name


class SearchEngine(models.Model):
    search_term = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)  # Allow empty descriptions
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Search Engines"  # Admin panel improvement

    def __str__(self):
        return self.search_term
