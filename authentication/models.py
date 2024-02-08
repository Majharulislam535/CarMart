from django.db import models
from django.contrib.auth.models import User
from Car_app.models import Car_Model
     
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    car = models.ForeignKey(Car_Model,on_delete=models.CASCADE)
    