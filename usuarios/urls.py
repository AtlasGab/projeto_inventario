from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='inicio'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('estoque/', views.estoque_view, name='estoque'),
    path('cadastro-material/', views.cadastro_material_view, name='cadastro_material'),
    path('entrada-material/', views.entrada_material_view, name='entrada_material'),
    path('retirada-material/', views.retirada_material_view, name='retirada_material'),
    path('emprestimo/', views.emprestimo_view, name='emprestimo'),
    path('devolucao/', views.devolucao_view, name='devolucao'),
    path('historico/', views.historico_view, name='historico'),
    path('relatorios/', views.relatorios_view, name='relatorios'),
    path('usuarios/', views.usuarios_view, name='usuarios'),
    path('logout/', views.logout_view, name='logout'),
]