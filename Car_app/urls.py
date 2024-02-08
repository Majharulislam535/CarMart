from django.urls import path,include
from .import views

urlpatterns = [
    
    path('details_car/<int:id>/', views.DetailsView.as_view(),name='details_car'),
     
]