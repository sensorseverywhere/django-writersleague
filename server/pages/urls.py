from django.urls import path

from .views import HomePageView, AboutPageView, ContactPageView, ThanksView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"), 
    path('about/', AboutPageView.as_view(), name="about"), 
    path('contact/', ContactPageView.as_view(), name="contact"),
    path('thanks/', ThanksView.as_view(), name="thanks"),
]