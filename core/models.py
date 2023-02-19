from django.db import models


# Create your models here.

class Product(models.Model):

    web_id = models.CharField(max_length = 25)
    slug = models.SlugField(max_length = 25)
    name = models.CharField(max_length = 25)
    description = models.TextField()
    is_active = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now = True, editable = False)
    

    class Meta:

        verbose_name_plural = "Products"

        


    def __str__(self):
        return self.name


    def display_text(self):
        return self.description[:50]




