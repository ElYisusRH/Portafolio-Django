from django.urls import path,include
from authentication.views import *

urlpatterns=[

    path("signup",SingUpView.as_view(),name="singup"),
    path("acoounts/",include("django.contrib.auth.urls"))
]