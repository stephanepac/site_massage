from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('presta',views.presta,name="presta"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about")
]