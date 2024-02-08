from django.db import models
from Brand.models import Brand_model
from django.contrib.auth.models import User

# Create your models here.
class Car_Model(models.Model):
     name = models.CharField(max_length=100)
     price=models.CharField(max_length=100)
     details= models.TextField()
     quantity = models.IntegerField()
     image = models.ImageField(upload_to='uploads/',blank=True,null=True)
     brand = models.ForeignKey(Brand_model,on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Car_Model,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comments by {self.name}'