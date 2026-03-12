from django.urls import path
from produtos import views

urlpatterns = [path("", views.exibir_catalogo, name="home")]
