from django.db import models

# Create your models here.
class Commission(models.Model):
    # Image property that is of type ImageField(<where the image is saved>)
    # In this case, the image is saved in a folder named images
    image = models.ImageField(upload_to='images')

    # Summary property that is of typeCharField(<maximum length of text>)
    summary = models.CharField(max_length=200)

    category = models.CharField(max_length=200)

    item = models.CharField(max_length=200)

    # Return summary when trying to describe object in admin page
    def __str__(self):
        return self.summary  