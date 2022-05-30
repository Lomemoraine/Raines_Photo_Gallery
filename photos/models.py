from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Category(models.Model):
    """ 
    category model acts as blueprint for all category instances
    """

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    cat_name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.cat_name
    
    def save_category(self):
        '''method to save category instance
        '''
        self.save()
        
    @classmethod
    def delete_category(cls, id):
        '''
        method to delete category instance
        '''
        return cls.objects.filter(id=id).delete()
    
    @classmethod
    def update_category(cls,current_value,new_value):
        fetched_object = Category.objects.filter(cat_name=current_value).update(cat_name=new_value)
        return fetched_object

    
class Location(models.Model):
    """
        blueprint class for all location instances
    """

    location = models.CharField(max_length=20, null=False, blank=False, default='Nairobi')

    def __str__(self):
        return self.location
    
    def save_location(self):
        '''method to save location instance
        '''
        self.save()
        
    @classmethod
    def delete_location(cls, id):
        '''
        method to delete location instance
        '''
        return cls.objects.filter(id=id).delete()
    
    @classmethod
    def update_location(cls,current_value,new_value):
        fetched_object = Location.objects.filter(location=current_value).update(location=new_value)
        return fetched_object



class Photo(models.Model):
    image = CloudinaryField('images/', default="", blank=True, null=True)
    image_name = models.CharField(max_length =60)
    image_description= models.TextField()
    image_location = models.ForeignKey(Location ,on_delete=models.CASCADE)
    image_category = models.ForeignKey(Category ,on_delete=models.CASCADE)

    
    def __str__(self):
        return self.image_name
    
    def save_image(self):
        return self.save()
    
    @classmethod
    def show_all_images(cls):
        return cls.objects.order_by("image_category")
    
    @classmethod
    def delete_image(cls, id):
        return cls.objects.filter(id=id).delete()
    
    @classmethod
    def get_image_by_id(cls, id):
        return cls.objects.filter(id=id).all()
    
    @classmethod
    def search_image_by_category(cls, search_term):
        album = cls.objects.filter(image_category__cat_name__icontains=search_term)
        return album

    @classmethod
    def update_image(cls,current_value,new_value):
        fetched_object = Photo.objects.filter(image_name=current_value).update(image_name=new_value)
        return fetched_object

    @classmethod
    def filter_by_location(cls,location):
        filtered_result = cls.objects.filter(image_location__location__icontains=location)
        return filtered_result