from django.test import TestCase
from .models import Category, Location, Photo
# Create your tests here.


class CategoryTestClass(TestCase):
    def setUp(self):
        '''
        method to create an instance of category everytime the tests are run
        '''
        self.category = Category(cat_name='CLOSE_UP')
        
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
        
    # def test_update_single_object_property(self):
    #     self.category.save_category()
    #     filtered_object =Category.update_category('Nature','CLOSE_UP')
    #     fetched = Location.objects.get(cat_name='CLOSE_UP')
    #     self.assertEqual(fetched.cat_name,'CLOSE_UP')
        
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
    def test_update_single_object_property(self):
        self.location.save_location()
        filtered_object =Location.update_location('Mombasa','Nairobi')
        fetched = Location.objects.get(location='Nairobi')
        self.assertEqual(fetched.location,'Nairobi')
        
class MyPhotos_TestCases(TestCase):
    def setUp(self):
        self.new_category = Category(cat_name='Nature')
        self.new_category.save_category()
        self.new_location = Location(location= 'Mombasa')
        self.new_location.save_location()
        self.new_image = Photo(id=1,image_name='raine photo', image_description='during attachment',image='/media/images/IMG_20210921_114451_347_3ZEprtH.jpg',image_category=self.new_category,image_location=self.new_location)
        
    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Photo.objects.all().delete()
        
    def test_is_instance(self):
        self.assertTrue(isinstance(self.new_image,Photo))
        self.assertTrue(isinstance(self.new_category,Category))
        self.assertTrue(isinstance(self.new_location,Location))
        
    def test_save_method(self):
        self.new_image.save_image()
        all_objects = Photo.objects.all()
        self.assertTrue(len(all_objects)>0)
        
    def test_delete_method(self):
        self.new_image.save_image()
        filtered_object = Photo.objects.filter(image_name='learn')
        Photo.delete_image(filtered_object)
        all_objects = Photo.objects.all()
        self.assertTrue(len(all_objects) == 0)
        
    def test_display_all_objects_method(self):
        self.new_image.save_image()
        all_objects = Photo.show_all_images()
        self.assertEqual(all_objects.image_name,'raine photo')
        
    def test_update_single_object_property(self):
        self.new_image.save_image()
        filtered_object =Photo.update_image('raine photo','gift photo')
        fetched = Photo.objects.get(image_name='gift photo')
        self.assertEqual(fetched.image_name,'gift photo')
        
    def test_get_image_by_id(self):
        self.new_image.save_image()
        fetched_image =Photo.get_image_by_id(1)
        self.assertEqual(fetched_image,1)
        
    def test_search_by_category(self):
        self.new_image.save_image()        
        fetch_specific = Category.objects.get(cat_name='Nature')
        self.assertTrue(fetch_specific.cat_name=='Nature')
    def test_filter_by_location(self):
        self.new_image.save_image()        
        fetch_specific = Location.objects.get(location='Mombasa')
        self.assertTrue(fetch_specific.location=='Mombasa')



