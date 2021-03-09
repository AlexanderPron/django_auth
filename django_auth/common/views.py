from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from common.forms import ProfileCreationForm
from django.http.response import HttpResponseRedirect
from common.models import UserProfile

class RegisterView(FormView):
  
    form_class = UserCreationForm
  
    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        login(self.request, authenticate(username=username, password=raw_password))
        return super(RegisterView, self).form_valid(form)
  
  
class CreateUserProfile(FormView):
  
    # form_class = ProfileCreationForm
    template_name = 'profile-create.html'
    success_url = reverse_lazy('common:login')
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            return HttpResponseRedirect(reverse_lazy('common:login'))
        return super(CreateUserProfile, self).dispatch(request, *args, **kwargs)
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return super(CreateUserProfile, self).form_valid(form)
  
  
def index(request):  
    context = {}
    if request.user.is_authenticated:
        curr_user = UserProfile.objects.get(user=request.user)
        context['username'] = request.user.username
        if curr_user.age:
            context['age'] = curr_user.age
        else:
            context['age'] = 0
    return render(request, 'index.html', context)
    
