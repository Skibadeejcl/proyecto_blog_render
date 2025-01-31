from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('indexavisos/', views.indexView, name='indexavisos'),
    path('login/', LoginView.as_view(next_page='dashboard'),name='login_url'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views.registerView, name='register_url'),
    path('register_tipo/', views.register_tipoView, name='register_tipo_url'),
    path('dashboard/', views.dashboardView, name='dashboard'),
    path('update_profile/', views.profile, name='update_profile'),
    path('new_cliente/', views.new_clienteView, name='new_cliente_url'),
    path('update_cliente/', views.clientes_update, name='update_cliente_url'),
    path('eliminar_cliente/', views.clientes_delete, name='delete_cliente_url'),
    # path('<int:clientes_id>', views.clientes_detail, name='cliente_detail'),
    # path('update_estado/', views.clientes_detail_edit, name='cliente_detail_edit'),

    path('<int:clientes_id>', views.clientes_detail, name='cliente_detail'),
    path('clientes/<int:clientes_id>/edit/', views.clientes_detail_edit, name='cliente_detail_edit'),


    path('set_adult_session/', views.set_adult_session, name='set_adult_session'),
    path('politicas_privacidad/', views.politicas_privacidad, name='politicas_privacidad'),

    path("ajax/load-comunas/", views.load_comunas, name="ajax_load_comunas"),

    path('clientes_lista/', views.lista_clientes, name='lista_clientes'),

    path('dashboard/<int:user_id>/', views.dashboardView, name='dashboard'),

    #password
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]

