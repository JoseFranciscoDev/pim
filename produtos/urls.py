from django.urls import path
from produtos import views

urlpatterns = [path("", views.listar_produtos, name="home")]
