from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView,TemplateView
from django.contrib.auth.views import LogoutView,LoginView,PasswordChangeView
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .import forms
from django.contrib import messages
from Car_app.models import Car_Model
from django.shortcuts import get_object_or_404
from .models import Order

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your models here.

 
class Register(CreateView):
    template_name='register.html'
    form_class=forms.RegisterForm
    success_url=reverse_lazy('home')

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['type']='Register'
        return context


class LogIn(LoginView):
    template_name='register.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['type']='LogIn'
        return context

class CustomLogOut(View):
    def get(self, request,):
        logout(request)
        return redirect('home')

@method_decorator(login_required,name='dispatch')
class EditProfile(UpdateView):
      template_name='edit.html'
      form_class=forms.ChangeUserData
      success_url=reverse_lazy('profile')

      def get_object(self,queryset=None):
        return self.request.user
      
      def form_valid(self, form):
        messages.success(self.request, 'Update Your Information Successfully')
        return super().form_valid(form)



@method_decorator(login_required,name='dispatch')
class passChange(PasswordChangeView):
    template_name='pass_change.html'
    form_class=PasswordChangeForm
    success_url=reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Password Change Successfully')
        return super().form_valid(form)



@login_required
def BuyNow(request, id):
    if request.method == 'POST':
            car = get_object_or_404(Car_Model, pk=id)
            if car.quantity > 0:
                car.quantity -= 1
                car.save()
                order = Order.objects.create(user=request.user, car=car)
                return redirect('profile')
            else:
                return redirect('profile')

    return render(request, 'car_details.html')


@login_required
def ProfileView(request):
    user_orders = Order.objects.filter(user=request.user)
    return render(request,'profile.html',{'orders':user_orders})