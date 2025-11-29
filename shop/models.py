from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    image = CloudinaryField('image', null=True, blank=True)
    description = models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0-show,1-Hidden")
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
 
    def __str__(self) :
        return self.name
  
  
 
class Product(models.Model):
    category =models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=150, null=False, blank=False)
    vendor = models.CharField(max_length=150, null=False, blank=False)
    product_image = CloudinaryField('image', null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False)
    original_price = models.FloatField(null=False, blank=False)
    selling_price = models.FloatField(null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0-show,1-Hidden")
    trending = models.BooleanField(default=False, help_text="0-default,1-Trending")
    slug = models.SlugField(unique=True, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_on']
 

 
    def __str__(self) :
        return self.name