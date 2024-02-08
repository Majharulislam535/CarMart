from django.shortcuts import render
from Brand.models import Brand_model
from Car_app.models import Car_Model


def home(request,brand_slug=None):
    
    car = Car_Model.objects.all()

    if brand_slug is not None:
        brand=Brand_model.objects.get(slug=brand_slug)
        car = Car_Model.objects.filter(brand=brand)
    
    brand = Brand_model.objects.all()
    return render(request,'index.html',{'brand':brand,'car':car})




# def home(request,category_slug=None):
#     post = Post.objects.all()
#     if category_slug is not None:
#         category=Category.objects.get(slug = category_slug)
#         post=Post.objects.filter(category=category)
   
       
#     category=Category.objects.all()

#     return render(request,'index.html',{'post':post,'category':category})