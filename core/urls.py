from django.urls import path

from . import views

urlpatterns = [
    path("",views.index , name="index"),
    path("setting/",views.asetting, name="setting"),
    path("upload/",views.upload, name="upload"),
    path("search",views.search, name="search"),
    path("follow/",views.follow, name="follow"),
    path("profile/<str:pk>/",views.profile, name="profile"),
    path("like-post/", views.like_post, name="like_post"),
    path("signup/",views.signup, name="signup"),
    path("login/",views.login, name="login"),
    path("logout/",views.logout, name="logout")
]
