from django.db import models

# Create your models here.
class Flan(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    short_name = models.SlugField()
    price = models.FloatField(default=4.990)
    is_private = models.BooleanField()
    


    def __str__(self):
        return self.name
    
class ContactForm(models.Model):
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()

    def __str__(self):
        return self.customer_email