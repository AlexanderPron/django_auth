from common.views import index, RegisterView, CreateUserProfile
from django.urls import path
from django.urls import reverse_lazy 
from django.contrib.auth.views import LoginView, LogoutView
  
app_name = 'common'  
urlpatterns = [  
    path('', index, name='index'),  
	path('login/', LoginView.as_view(template_name='login.html'), name='login'),
	path('logout/',  LogoutView.as_view(), name='logout'),
	path('register/', RegisterView.as_view(template_name='register.html', 
		success_url=reverse_lazy('common:profile-create')),
		name='register'),  
  path('profile-create/', CreateUserProfile.as_view(), name='profile-create'),
]