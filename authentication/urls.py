from django.urls import path
from authentication.views import *


urlpatterns=[

    path("",SingUpView.as_view(),name="singup"),
]