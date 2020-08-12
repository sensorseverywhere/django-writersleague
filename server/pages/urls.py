from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
    path(
        '',
        views.ComingSoonPageView.as_view(),
        name="coming-soon"
        ),
    path(
        'temphomepage/',
        views.HomePageView.as_view(),
        name="home"
        ),
    # path(
    #     'about/',
    #     views.AboutPageView.as_view(),
    #     name="about"
    #     ),
    # path(
    #     'contact/',
    #     views.ContactFormView.as_view(),
    #     name="contact"
    #     ),
    # path(
    #     'thanks/',
    #     views.ThanksPageView.as_view(),
    #     name="thanks"
    #     ),
]
