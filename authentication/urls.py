from django.urls import path
from .import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/',views.Register.as_view(),name='Registration'),
    path('login/',views.LogIn.as_view(),name='login'),
    path('LogOut/',views.CustomLogOut.as_view(),name='LogOut'),
    path('profile/',views.ProfileView,name='profile'),
    path('edit_profile/',views.EditProfile.as_view(),name='edit_profile'),
    path('passChange/',views.passChange.as_view(),name='passChange'),
    path('buy_now/<int:id>/',views.BuyNow, name='buy_now'),
     
]

