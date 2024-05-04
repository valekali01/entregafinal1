
from django.urls import path

from .views import (
    
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
    avatar_view,
<<<<<<< HEAD

    create_user,
    home_view,
=======
    create_user,
>>>>>>> 423d5c0dfb256613d46bbc159d01748e21b02814
    ReservaListView,
    ReservaDetailView,
    ReservaDeleteView,
    ReservaUpdateView,
<<<<<<< HEAD
    ReservaCreateView,
    user_login_view,
    user_logout_view,
    UserUpdateView,
    reserva_search_view,
    # ------------------------------------------------------------------------
    # Clase 25
    # ------------------------------------------------------------------------
    avatar_view,
=======
    ReservaCreateView,    
    UserUpdateView,
    reserva_search_view,
    
>>>>>>> 423d5c0dfb256613d46bbc159d01748e21b02814
    
)

urlpatterns = [
    path("", home_view, name="home"),
    path("sala/list/", SalaListView.as_view(), name="sala-list"),
    path("sala/create/", SalaCreateView.as_view(), name="sala-create"),
    path("sala/<int:pk>/detail/", SalaDetailView.as_view(), name="sala-detail"),
    path("sala/<int:pk>/delete/", SalaDeleteView.as_view(), name="sala-delete"),
    path("sala/<int:pk>/update/", SalaUpdateView.as_view(), name="sala-update"),
    path('sala/buscar', sala_search_view, name="sala-buscar"),
    path('editar-perfil/', UserUpdateView.as_view(), name='editar-perfil'),
    path('create_user/', create_user, name='create_user'),
    path("reserva/list/", ReservaListView.as_view(), name="reserva-list"),
    path("reserva/create/", ReservaCreateView.as_view(), name="reserva-create"),
    path("reserva/<int:pk>/detail/", ReservaDetailView.as_view(), name="reserva-detail"),
    path("reserva/<int:pk>/delete/", ReservaDeleteView.as_view(), name="reserva-delete"),
    path("reserva/<int:pk>/update/", ReservaUpdateView.as_view(), name="reserva-update"),
    path('reserva/buscar', reserva_search_view, name="reserva-buscar"),
    path("login/", user_login_view, name="login"),
    path("logout/", user_logout_view, name="logout"),
    path('editar-perfil/', UserUpdateView.as_view(), name='editar-perfil'),
    path('avatar/add/', avatar_view, name='avatar_add'),
<<<<<<< HEAD

    path("", home_view, name="home"),
    path('create_user/', create_user, name='create_user'),
    path("reserva/list/", ReservaListView.as_view(), name="reserva-list"),
    path("reserva/create/", ReservaCreateView.as_view(), name="reserva-create"),
    path("reserva/<int:pk>/detail/", ReservaDetailView.as_view(), name="reserva-detail"),
    path("reserva/<int:pk>/delete/", ReservaDeleteView.as_view(), name="reserva-delete"),
    path("reserva/<int:pk>/update/", ReservaUpdateView.as_view(), name="reserva-update"),
    path('reserva/buscar', reserva_search_view, name="reserva-buscar"),
    path("login/", user_login_view, name="login"),
    path("logout/", user_logout_view, name="logout"),
    path('editar-perfil/', UserUpdateView.as_view(), name='editar-perfil'),
    # ------------------------------------------------------------------------
    # Clase 25
    # ------------------------------------------------------------------------
    path('avatar/add/', avatar_view, name='avatar_add'),
=======
>>>>>>> 423d5c0dfb256613d46bbc159d01748e21b02814
    
]





