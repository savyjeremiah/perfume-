from django.db import models

class Perfume(models.Model):
    CATEGORY_CHOICES = [
        ('Designers Perfume Oil', 'Designers Perfume Oil'),
        ('Suratti Perfume Oils', 'Suratti Perfume Oils'),
        ('Naseem Oils', 'Naseem Oils'),
    ]
    
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=150, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='perfume_images/', blank=True, null=True)
    available = models.BooleanField(default=True)
    grams = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, help_text="Weight of the product in grams")

    class Meta:
        verbose_name_plural = "Perfumes"

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
