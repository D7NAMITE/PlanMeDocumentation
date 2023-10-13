import firebase_admin
from firebase_admin import credentials
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import firebase_admin
from firebase_admin import auth
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView


cred = credentials.Certificate('/planme/planme/users/planme-6007f-firebase-adminsdk-vcf83-4089971acc.json')
firebase_admin.initialize_app(cred)

@csrf_exempt
def verify_token(request):
    token = request.POST.get('token')

    try:
        # Verify the token against Firebase Admin SDK
        decoded_token = auth.verify_id_token(token)
        uid = decoded_token['uid']
        return JsonResponse({"status": "success", "uid": uid})

    except ValueError:
        # Token is invalid
        return JsonResponse({"status": "error", "message": "Invalid token"})


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
