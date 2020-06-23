
#Django
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
#from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DetailView, ListView

#Exceptios
#from django.db.utils import IntegrityError

#models
from django.contrib.auth.models import User

#Forms

from people.forms import AdviserRegisterForm, AdviserUpdateForm, AdviserListForm

#models
from people.models import Advisers

@login_required
def adviser_register(request):
    """login view"""
    if request.method == "POST":
        print(request.POST)
        form  = AdviserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
        
    else:
        form = AdviserRegisterForm()

    return render(
        request, 
        'people/advisers_register.html',
        context={'form': form}
        )


@login_required
def adviser_update(request):
    """logout user"""
    if request.method == "POST":
        print(request.POST)
        form  = AdviserUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('people:adviser_list')
    else:
        form = AdviserUpdateForm()
    return render(
        request, 
        'people/advisers_update.html',
        context={'form': form}
    )


#@login_required
class AdviserListView(LoginRequiredMixin,ListView):
    """Return all advisers registered."""

    template_name = 'people/advisers_list.html'
    model = Advisers
    ordering = ('-created',)
    paginate_by = 30
    context_object_name = 'advisers'



