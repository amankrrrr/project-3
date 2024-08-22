from django.shortcuts import render, redirect
from .models import Inventory
from .forms import ClientForm, InventoryLoginForm, InventoryAddForm, InventoryUpdateForm
from django.db import models  

# Create your views here.


from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    FormView
)

from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login



class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    form_class = InventoryLoginForm

    def get_success_url(self):
        return reverse_lazy('InventoryList')


class RegisterPage(FormView):
    form_class = ClientForm
    success_url = reverse_lazy('InventoryList')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)


    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('InventoryList')

        return super(RegisterPage, self).get(*args, **kwargs)


class Index(ListView):
    model = Inventory
    context_object_name = 'index'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['index'] = context['index'].filter(user=all)
        context['count_incomplete'] = context['index'].filter(complete=False).count()
        context['count_complete'] = context['index'].filter(complete=True).count()
        context['count_total'] = context['count_incomplete'] + context['count_complete']

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['index'] = context['index'].filter(title__startswith=search_input)
        context['search_input'] = search_input
        context['desc'] = context['index'].filter(description=None)

        return context
    

class InventoryList(LoginRequiredMixin, ListView):
    model = Inventory
    context_object_name = 'Inventory_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        inventory_list = context['Inventory_list'].filter(user=self.request.user)
        context['Inventory_list'] = inventory_list
        # context['Inventory_list'] = context['Inventory_list'].filter(user=self.request.user)
        context['count_incomplete'] = context['Inventory_list'].filter(complete=False).count()
        context['count_complete'] = context['Inventory_list'].filter(complete=True).count()
        context['count_total'] = context['count_incomplete'] + context['count_complete']
        context['total_value'] = inventory_list.aggregate(total_value=models.Sum('value'))['total_value'] or 0
        context['zero_quantity_count'] = inventory_list.filter(quantity=0).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['Inventory_list'] = context['Inventory_list'].filter(title__startswith=search_input)
        context['search_input'] = search_input

        return context
    


class InventoryAdd(LoginRequiredMixin, CreateView):
    form_class = InventoryAddForm
    model = Inventory
    success_url = reverse_lazy('InventoryList')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(InventoryAdd, self).form_valid(form)
    


class InventoryDetail(LoginRequiredMixin, DetailView):
    model = Inventory
    context_object_name = 'InventoryDetail'
    

class InventoryDelete(LoginRequiredMixin, DeleteView):
    model = Inventory
    success_url = reverse_lazy('InventoryList')
    context_object_name = 'InventoryDelete'
    
    
class InventoryUpdate(LoginRequiredMixin, UpdateView):
    model = Inventory
    form_class = InventoryUpdateForm
    success_url = reverse_lazy('InventoryList')
