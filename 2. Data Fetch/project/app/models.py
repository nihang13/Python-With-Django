from django.db import models

# Create your models here.
class Course(models.Model):
    image=models.ImageField(upload_to="images") #pip install pillow
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    price=models.IntegerField()

    def __str__(self):
        return self.title

     