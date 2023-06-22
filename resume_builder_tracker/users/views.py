from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from .forms import CustomUserCreationForm


class UserRegistrationView(FormView):
    template_name = 'users/registration.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        print("form valid")
        form.save()
        return redirect(self.get_success_url())
    
    def form_invalid(self, form):
    # Handle form validation errors here
    # You can add custom logic or error handling
        print(form.errors)
        return super().form_invalid(form)


class UserLoginView(FormView):
    template_name = 'users/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('core:dashboard')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        # Handle form validation errors here
        # You can add custom logic or error handling
        print(form.errors)
        return super().form_invalid(form)


@login_required
def user_logout(request):
    logout(request)
    return redirect('users:login')


# @login_required
# def account_settings(request):
#     user = request.user
#     if request.method == 'POST':
#         form = PasswordChangeForm(user, request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('user:account_settings')
#     else:
#         form = PasswordChangeForm(user)

#     return render(request, 'user/account_settings.html', {'form': form})


# class CustomPasswordChangeView(PasswordChangeView):
#     template_name = 'user/password_change.html'
#     success_url = reverse_lazy('user:password_change_done')
