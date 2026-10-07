
from django.urls import path
from slot_v2.views import SignUpView,BookingV2ListCreateView,Bookinv2RetrieveUpdateDeleteView

urlpatterns = [

    # autheriztion route
    path("signup/",SignUpView.as_view()),

    # bookingv2 list,create route
    path("slotv2/",BookingV2ListCreateView.as_view()),

    # booking v2 retrieve,update,delete route
    path("slotv2/<int:pk>/",Bookinv2RetrieveUpdateDeleteView.as_view()),
]

