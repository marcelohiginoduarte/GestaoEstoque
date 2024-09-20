from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_produtos, name='listar_produtos'),
    path('movimentacao/<int:produto_id>/', views.movimentacao_estoque, name='movimentacao_estoque'),
]