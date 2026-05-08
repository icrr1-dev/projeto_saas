from django.contrib import admin
from django.urls import path

from core_loja import views


urlpatterns = [

    path('admin/', admin.site.urls),

    path(
        'loja/<int:empresa_id>/',
        views.dashboard_loja,
        name='url_da_loja'
    ),

    path(
        'loja/<int:empresa_id>/novo-cliente/',
        views.cadastrar_item,
        {'tipo': 'cliente'},
        name='novo_cliente'
    ),

    path(
        'loja/<int:empresa_id>/novo-produto/',
        views.cadastrar_item,
        {'tipo': 'produto'},
        name='novo_produto'
    ),
]