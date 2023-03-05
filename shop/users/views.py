from django.contrib.auth.views import LoginView
# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView
from users.forms import UserAuthForm, UserRegistrationForm, UserProfileForm
from users.models import Usery



class UserLoginView(LoginView):
    template_name = 'users/authen.html'
    form_class = UserAuthForm
    def get_success_url(self):
        return reverse_lazy('index')

class UserRegistrationView(CreateView):
    model = Usery
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('authen')



class UserProfileView(UpdateView):
    model = Usery
    form_class = UserProfileForm
    template_name = 'users/profille.html'
    def get_success_url(self):
        return reverse_lazy('profille', args=(self.request.user.id,))



class UserLoginView(LoginView):
    template_name = 'users/authen.html'
    form_class = UserAuthForm

    def get_success_url(self):
        return reverse_lazy('index')



