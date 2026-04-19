from django.urls import path, re_path
from . import views
from django.views.generic import RedirectView

urlpatterns=[

path("login/",views.login,name="login"),
path("chat/",views.chat,name="chat"),
re_path(r"^.*$",RedirectView.as_view(url="/login/"))


    ]
