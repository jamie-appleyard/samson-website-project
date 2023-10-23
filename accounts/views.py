from django.shortcuts import render, redirect
from django.http import request, response, HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from accounts.models import CustomUser, UserType, VettingStatus
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm

#Email verification related imports
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage


def SignUpView(request):
    if request.method =='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            user_type = UserType(user_type=0, user=request.user)
            user_type.save()
            logged_in_user = request.user
            logged_in_user.email_verified = True
            logged_in_user.save()
            vetting_status = VettingStatus(vetting_status=0, user=request.user)
            vetting_status.save()
            return redirect('home')
        else:
            return render(request, "registration/signup.html", context={'form':form})
    else:
        form = CustomUserCreationForm()
        context = {
            "form" : form
        }
        return render(request, "registration/signup.html", context)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode((uidb64)))
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.email_verified = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return HttpResponse('Activation link is invalid!')