from django.db import models
import datetime as dt
# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length =30)
    

    def __str__(self):
        return self.location_name
    
    class Meta:
        ordering = ['location_name']
        
    def save_location(self):
        self.save()

    


class Category(models.Model):
    category_name = models.CharField(max_length =30, unique=True)

    def __str__(self):
        return self.category_name
    
    def save_category(self):
        self.save()

    class Meta:
        ordering = ['category_name']

class Image(models.Model):
    img_name = models.CharField(max_length = 30)
    img_description = models.CharField(max_length = 255)
    img_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'imgur/',default='DEFAULT VALUE')
    img_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    img_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.img_location)

    def save_image(self):
        self.save()

    @classmethod
    def get_all_images(cls):
        image = cls.objects.all()
        return image
    
    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id=id)
        return image
    
    @classmethod
    def delete_image_by_id(cls,id):
        image = cls.objects.remove(id=id)
        return image
    
    @classmethod
    def update_image_by_id(cls,id):
        image = cls.objects.update(id=id)
        return image
    
    @classmethod
    def search_by_location_id(cls,search_term):
        image = Image.objects.filter(img_location__id=search_term).all()
        return image
    
    @classmethod
    def search_by_category(cls,search_term):
        image = Image.objects.filter(img_category__category_name__icontains=search_term).all()
        return image
