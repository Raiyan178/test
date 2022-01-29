from email.policy import default
from django.db import models
from .validators import validate_file_extension
import django.utils.timezone
# Create your models here.


class Category(models.Model):
    Cat=models.CharField(max_length=20)

    def __str__(self):
        return self.Cat



class UploadPortfolio(models.Model):
    title=models.CharField(max_length=50)
    discription=models.CharField(max_length=1000)
    catagory=models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    thumbnail=models.ImageField(blank=False,upload_to='thumbnail')
    ThreeD=models.FileField(upload_to='3d',validators=[validate_file_extension],blank=True)
    upload_date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title



class client(models.Model):
    name=models.CharField(max_length=100)
    commentcl=models.CharField(max_length=200)
    imgcl=models.ImageField(upload_to='clientimg',default='climg/t1.jpg')
    ratecl=models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
