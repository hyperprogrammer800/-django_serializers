from django.db import models
from PIL import Image
# Create your models here.
class productMainModel(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    uniquecode = models.BooleanField(default=True)
    sizetype = models.TextChoices('sizetype','10 20 30')
    size = models.CharField(blank=True, choices=sizetype.choices,max_length=5)
    qualitytype = models.TextChoices('qualitytype','high low medium')
    quality = models.CharField(blank=True, choices=qualitytype.choices,max_length=10)

    def __str__(self):
        return self.title

class productColourModel(models.Model):
    product = models.ForeignKey(productMainModel,on_delete=models.CASCADE, related_name='colour')
    colourtype = models.TextChoices('colourtype','red blue green black')
    colour = models.CharField(choices=colourtype.choices,max_length=10)
    def __str__(self):
        return self.colour

class productImageModel(models.Model):
    product = models.ForeignKey(productMainModel,on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    def __str__(self):
        return self.image.url
