from django.urls import path
from .views import home
from django.views.generic import TemplateView

urlpatterns = [
    path('', home, name='home'),
    path("googleca93744ea4f1f4c3.html", TemplateView.as_view(template_name="googleca93744ea4f1f4c3.html"), name="google-site-verification"),
]
