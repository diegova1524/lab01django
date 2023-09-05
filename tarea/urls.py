from django.urls import path
from . import views

urlpatterns = [
    path('sumar/<int:uno>/<int:dos>',views.sumar,name="sumar"),
    path('restar/<int:uno>/<int:dos>',views.restar,name="restar"), 
    path('multiplicar/<int:uno>/<int:dos>',views.multiplicar,name="multiplicar"),  
]
