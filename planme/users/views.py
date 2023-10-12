import pyrebase
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView


config = {
  "apiKey": "AIzaSyDRLf6GEoHKnQcHzf8Nh4bhO8e13r0iiVI",
  "authDomain": "planme-6007f.firebaseapp.com",
  "projectId": "planme-6007f",
  "storageBucket": "planme-6007f.appspot.com",
  "messagingSenderId": "409452142687",
  "appId": "1:409452142687:web:e6eb0572b53dac1ce1fbea",
  "measurementId": "G-P806F77297"
}

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert self.request.user.is_authenticated  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()


firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

def login(request):
    return render(request, "login.html")

def home(request):
    return render(request, "home.html")

def post_login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        user = auth.sign_in_with_email_and_password(email, password)
    except:
        message = "Invalid Account!! Please check your email or password."
        return render(request, "login.html", {"message": message})
    # the user's Firebase ID token is retrieved and stored in Django session.
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    return render(request, 'home.html')

def logout(request):
    request.session.pop('uid', None)
    return redirect('login.html')

def signup(request):
    return render(request, "signup.html")

def post_signup(request):
     email = request.POST.get('email')
     password = request.POST.get('password')
     try:
        # creating a user with the given email and password
        auth.create_user_with_email_and_password(email,password)
     except:
        # return to the signup page.
        return render(request, "signup.html")
     return render(request, "Login.html")
