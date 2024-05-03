
from django.urls import path

from .views import (
    create_user,
    home_view,
    SalaListView,
    SalaDetailView,
    SalaDeleteView,
    SalaUpdateView,
    SalaCreateView,
    user_login_view,
    user_logout_view,
    UserUpdateView,
    sala_search_view,
    # ------------------------------------------------------------------------
    # Clase 25
    # ------------------------------------------------------------------------
    avatar_view,
    reserva_list, 
    reserva_detail, 
    reserva_create, 
    reserva_update, 
    reserva_delete,
)

urlpatterns = [
    path("", home_view, name="home"),
    path('create_user/', create_user, name='create_user'),
    path("sala/list/", SalaListView.as_view(), name="sala-list"),
    path("sala/create/", SalaCreateView.as_view(), name="sala-create"),
    path("sala/<int:pk>/detail/", SalaDetailView.as_view(), name="sala-detail"),
    path("sala/<int:pk>/delete/", SalaDeleteView.as_view(), name="sala-delete"),
    path("sala/<int:pk>/update/", SalaUpdateView.as_view(), name="sala-update"),
    path('sala/buscar', sala_search_view, name="sala-buscar"),
    path("login/", user_login_view, name="login"),
    path("logout/", user_logout_view, name="logout"),
    path('editar-perfil/', UserUpdateView.as_view(), name='editar-perfil'),
    # ------------------------------------------------------------------------
    # Clase 25
    # ------------------------------------------------------------------------
    path('avatar/add/', avatar_view, name='avatar_add'),
    path('reservas/', reserva_list, name='reserva-list'),
    path('reservas/<int:pk>/', reserva_detail, name='reserva-detail'),
    path('reservas/create/', reserva_create, name='reserva-create'),
    path('reservas/<int:pk>/update/', reserva_update, name='reserva-update'),
    path('reservas/<int:pk>/delete/', reserva_delete, name='reserva-delete'),
    
]





