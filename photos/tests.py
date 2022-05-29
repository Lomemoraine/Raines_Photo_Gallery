from django.test import TestCase
from .models import Category, Location, Photo
# Create your tests here.


class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(name='CLOSE_UP')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))
        
    def test_save_method(self):
        self.category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)