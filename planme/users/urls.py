from django.urls import path
from planme.users.views import user_detail_view, user_redirect_view, user_update_view
from . import views

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path('login/', views.login, name="login"),
    path('', views.home, name="home"),
    path('postlogin/', views.post_login),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('postsignup/', views.post_signup),
]
