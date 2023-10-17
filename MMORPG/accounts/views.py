from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserRegisterForm,UserLoginForm
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.models import Group


class UserRegisterView(SuccessMessageMixin, CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('board')
    template_name = 'accounts/signup.html'



class UserLoginView(SuccessMessageMixin, LoginView):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'
    next_page = 'board'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация на сайте'
        return context


class UserLogoutView(LogoutView):
    template_name = 'accounts/logout.html'
    next_page = 'board'


