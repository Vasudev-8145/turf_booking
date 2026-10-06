
from django.urls import path
from slot_v2.views import SignUpView,BookingV2ListCreateView

urlpatterns = [

    # autheriztion route
    path("signup/",SignUpView.as_view()),

    # bookingv2 list,create route
    path("slotv2/",BookingV2ListCreateView.as_view()),
]

