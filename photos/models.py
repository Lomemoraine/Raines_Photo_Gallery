from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Location(models.Model):
    """
        blueprint class for all location instances
    """

    location = models.CharField(max_length=20, null=False, blank=False, default='Nairobi')

    def __str__(self):
        return self.location

class Category(models.Model):
    """ 
    category model acts as blueprint for all category instances
    """

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    image = models.ImageField(upload_to = 'images/', blank=True, null=True)
    image_name = models.CharField(max_length =60)
    image_description= models.TextField()
    image_location = models.ForeignKey(Location ,on_delete=models.CASCADE)
    image_category = models.ForeignKey(Category ,on_delete=models.CASCADE)

    
    def __str__(self):
        return self.image
    
    def save_image(self):
        return self.save()
    
    @classmethod
    def show_all_images(cls):
        return cls.objects.order_by("image_category")
    
    @classmethod
    def delete_image(cls, id):
        return cls.objects.filter(id=id).delete()
