from django.urls import path
from Usuarios.views import logout
from .views import actualizarSubcategoria, eliminarCategoria, eliminarSubcategoria, home,actualizar, registrar, eliminar, productos, categorias, registrarSubcategoria, subcategorias, registrarCategoria, actualizarCategoria
urlpatterns = [
    path('home', home, name='Home'),
    path('Productos/',productos, name='Productos'),
    path('Productos/RegistrarProducto/',registrar, name='Registrar Producto'),
    path('Productos/ActualizarProducto/<int:id>',actualizar, name='Actualizar Producto'),
    path('Productos/EliminarProducto/<int:id>',eliminar, name='Eliminar Producto'),
    path('Categorias/',categorias, name='Categorias'),
    path('Categorias/RegistrarCategoria/',registrarCategoria, name='Registrar Categoria'),
    path('Categorias/ActualizarCategoria/<int:id>',actualizarCategoria, name='Actualizar Categoria'),
    path('Categorias/EliminarCategoria/<int:id>',eliminarCategoria, name='Eliminar Categoria'),
    path('Subcategorias/',subcategorias, name='Subcategorias'),
    path('Subcategorias/RegistrarSubcategoria/',registrarSubcategoria, name='Registrar Subcategoria'),
    path('Subcategorias/ActualizarSubcategoria/<int:id>',actualizarSubcategoria, name='Actualizar Subcategoria'),
    path('Subcategorias/EliminarSubcategoria/<int:id>',eliminarSubcategoria, name='Eliminar Subcategoria'),
    path('cerrarSesion',logout, name='Cerrar Sesion'),
]