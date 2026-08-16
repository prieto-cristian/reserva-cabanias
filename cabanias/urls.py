from django.urls import path
from . import views

urlpatterns = [
    path("", views.CabaniaListView.as_view(), name="listar_cabanias"),
    path("cabania/<int:pk>/", views.ReservaCreateView.as_view(),
         name="detalle_reserva"),
    path("reserva-enviada/", views.reserva_enviada, name="reserva_enviada"),
]