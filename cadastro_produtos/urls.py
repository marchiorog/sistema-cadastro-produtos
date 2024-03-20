from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.produto, name='produto'),
    path('exibir_produto/', views.exibir_produto, name='exibir_produto'),
    path('comentario/<int:produto_id>/', views.comentario, name='comentario'),
    path('deletar-produto/<int:produto_id>/', views.deletar_produto, name='deletar_produto'),
    path('deletar-comentario/<int:comentario_id>/', views.deletar_comentario, name='deletar_comentario'),
] 
