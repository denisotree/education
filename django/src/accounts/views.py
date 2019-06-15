from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy

from django.views.generic import CreateView

from .models import AccountUser
from .forms import LoginForm, RegisterForm


def login_view(request):
    form = LoginForm

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        success_url = reverse('main:main')

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(
                username=username,
                password=password,
            )

            if user and user.is_active:
                login(request, user)
                return redirect(success_url)

    return render(
        request,
        'accounts/login.html',
        {'form': form}
    )


class AccountLoginView(LoginView):
    template_name = 'accounts/register.html'


class RegistrationView(CreateView):
    model = AccountUser
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('products:products')
    form_class = RegisterForm

    def post(self, *args, **kwargs):
        response = super(RegistrationView, self).post(*args, **kwargs)
        obj = self.object
        login(self.request, obj)
        return response


def register_view(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        success_url = reverse('main:main')

        if form.is_valid():
            if form.clear_password_confirm():
                user = form.save(commit=False)
                user.is_active = True
                user.save()

                if user and user.is_active:
                    login(request, user)
                    return redirect(success_url)

    return render(
        request,
        'accounts/register.html',
        {'form': form}
    )
