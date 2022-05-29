from django.test import TestCase
from .models import Category, Location, Photo
# Create your tests here.


class CategoryTestClass(TestCase):
    def setUp(self):
        '''
        method to create an instance of category everytime the tests are run
        '''
        self.category = Category(name='CLOSE_UP')
        
    def test_instance(self):
        '''
        method to check whether the instance created is actually of model category
        '''
        self.assertTrue(isinstance(self.category, Category))
        
    def test_save_method(self):
        '''
        method to test if categories are being saved
        '''
        self.category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)
        
    def test_delete_method(self):
        '''
        method to test whether category created can be deleted
        '''
        Category.delete_category(self.category.id)
        categories =Category.objects.all()
        self.assertTrue(len(categories) == 0)
        
class LocationTestClass(TestCase):
    def setUp(self):
        '''
        method to create an instance of location everytime the tests are run
        '''
        self.location = Location(location='Mombasa')
        
    def test_instance(self):
        '''
        method to check whether the instance created is actually of model Location
        '''
        self.assertTrue(isinstance(self.location, Location))
        
    def test_save_method(self):
        '''
        method to test if locations are being saved
        '''
        self.location.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)
        
    def test_delete_method(self):
        '''
        method to test whether location added can be deleted
        '''
        Location.delete_location(self.location.id)
        locations =Category.objects.all()
        self.assertTrue(len(locations) == 0)