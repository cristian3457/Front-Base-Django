from Usuarios.services import actualizarPassword, valida_token
from django.shortcuts import redirect, render
from .services import get_subcategoriasID,eliminar_subcategoria, eliminar_categoria, eliminar_producto, get_productos, get_producto, registrar_producto, actualizar_producto, get_categorias, get_subcategorias, registrar_categoria, get_categoria, actualizar_categoria, actualizar_subcategoria, registrar_subcategoria, get_subcategoria


# Create your views here.
def validar_token(funcion_parametro):
    def funcion_interior(request):
        if request.session['usuario'] and request.session['token']:
            datos = {
                'usuario':request.session['usuario']['username'],
                'token': request.session['token']
            }
            respuesta = valida_token(datos)
            if respuesta['response']:
                return funcion_parametro(request)
            else:
                return redirect('/')
        else:
            return redirect('/')
    return funcion_interior

def validar_token_(funcion_parametro):
    def funcion_interior(request,id):
        if request.session['usuario'] and request.session['token']:
            datos = {
                'usuario':request.session['usuario']['username'],
                'token': request.session['token']
            }
            respuesta = valida_token(datos)
            if respuesta['response']:
                return funcion_parametro(request,id)
            else:
                return redirect('/')
        else:
            return redirect('/')
    return funcion_interior

@validar_token
def home(request):
    token = request.session['token']
    if request.method == 'POST':
        password = request.POST.get("password")
        username = request.session['usuario']['username']
        id = request.session['usuario']['id']
        respuesta = actualizarPassword(id,username, password, token)
        if respuesta:
            return render(request,'home.html',{'actualizado':True})
    return render(request,'home.html')
@validar_token_
def actualizar(request, id):
    token = request.session['token']
    producto = get_producto(id, token)
    categorias = get_categorias(token)
    subcategorias = get_subcategoriasID(token)
    cadenatemp = ""
    cadena = ""
    contadorCat = 0
    contadorSubcat = 0
    for c in categorias:
        cadenatemp = ""
        contadorCat+=1
        for s in subcategorias:
            contadorSubcat += 1
            if c["id"] == s["categoria"]:
                if contadorSubcat == len(subcategorias):
                    cadenatemp += s["subcategoria"]
                else:
                    cadenatemp += s["subcategoria"] + ","
        if contadorCat == len(categorias):
            if len(cadenatemp) > 0:
                cadena += str(c["id"]) + ":" + cadenatemp
        else:
            if len(cadenatemp) > 0:
                cadena += str(c["id"]) + ":" + cadenatemp + "-"
    if request.method == 'POST':
        subcategoria = request.POST.get("subcategorias")
        idsubcat = 0
        for s in subcategorias:
            if s['subcategoria'] == subcategoria:
                idsubcat = s['id']
                break
        if 'img' in request.FILES:
            producto = {
                "producto":request.POST.get("nombre"),
                "precio":request.POST.get("precio"), 
                "descripcion": request.POST.get("descripcion"),
                "img":request.POST.get("base64"),
                "categoria":request.POST.get("categoria"),
                "subcategoria":idsubcat,
            }
        else: 
            producto = {
                "producto":request.POST.get("nombre"),
                "precio":request.POST.get("precio"), 
                "descripcion": request.POST.get("descripcion"),
                "categoria":request.POST.get("categoria"),
                "subcategoria":idsubcat,
            }
        actualizar_producto(id, producto, token)
        return redirect('/Productos/')
    return render(request,'actualizarProducto.html',{'producto':producto,'operacion':'Actualizar', 'categorias':categorias,'subcategorias':cadena})
@validar_token
def registrar(request):
    token = request.session['token']
    categorias = get_categorias(token)
    subcategorias = get_subcategoriasID(token)
    cadenatemp = ""
    cadena = ""
    contadorCat = 0
    contadorSubcat = 0
    for c in categorias:
        cadenatemp = ""
        contadorCat+=1
        print('contadorSubcat:',contadorSubcat)
        for s in subcategorias:
            contadorSubcat += 1
            if c["id"] == s["categoria"]:
                print('count:',subcategorias.count(c["id"]))
                if contadorSubcat == subcategorias.count(c["id"]):
                    cadenatemp += s["subcategoria"]
                else:
                    cadenatemp += s["subcategoria"] + ","
        if contadorCat == len(categorias):
            if len(cadenatemp) > 0:
                cadena += str(c["id"]) + ":" + cadenatemp
        else:
            if len(cadenatemp) > 0:
                cadena += str(c["id"]) + ":" + cadenatemp + "-"
    print('cadena:',cadena)
    if request.method == 'POST' and 'img' in request.FILES:
        subcategoria = request.POST.get("subcategorias")
        idsubcat = 0
        for s in subcategorias:
            if s['subcategoria'] == subcategoria:
                idsubcat = s['id']
                break
        producto = {
            "producto":request.POST.get("nombre"),
            "precio":request.POST.get("precio"), 
            "descripcion": request.POST.get("descripcion"),
            "img":request.POST.get("base64"),
            "categoria":request.POST.get("categoria"),
            "subcategoria":idsubcat,
            }
        registrar_producto(producto, token)
        return redirect('/Productos/')
    return render(request,'actualizarProducto.html',{'operacion':'Registrar', 'categorias':categorias,'subcategorias':cadena})
@validar_token_
def eliminar(request, id):
    token = request.session['token']
    eliminar_producto(id, token)
    return redirect('/Productos/')
@validar_token
def productos(request):
    token = request.session['token']
    productos = get_productos(token)
    return render(request,'productos.html',{'productos':productos})
@validar_token
def categorias(request):
    token = request.session['token']
    categorias = get_categorias(token)
    return render(request,'categorias.html',{'categorias':categorias})
@validar_token_
def actualizarCategoria(request, id):
    token = request.session['token']
    categoria = get_categoria(id, token)
    if request.method == 'POST':
        if 'img' in request.FILES:
            categoria = {
                "categoria":request.POST.get("categoria"), 
                "descripcion": request.POST.get("descripcion"),
                "img":request.POST.get("base64"),
            }
        else: 
            categoria = {
                "categoria":request.POST.get("categoria"),
                "descripcion": request.POST.get("descripcion")
            }
        actualizar_categoria(id, categoria, token)
        return redirect('/Categorias/')
    return render(request,'operacionesCategoria.html',{'categoria':categoria,'operacion':'Actualizar'})
@validar_token
def registrarCategoria(request):
    token = request.session['token']
    if request.method == 'POST' and 'img' in request.FILES:
        categoria = {
            "categoria":request.POST.get("categoria"),
            "descripcion": request.POST.get("descripcion"),
            "img":request.POST.get("base64"),
            }
        registrar_categoria(categoria, token)
        return redirect('/Categorias/')
    return render(request,'operacionesCategoria.html',{'operacion':'Registrar'})
@validar_token_
def eliminarCategoria(request, id):
    token = request.session['token']
    eliminar_categoria(id, token)
    return redirect('/Categorias/')

@validar_token
def subcategorias(request):
    token = request.session['token']
    subcategorias = get_subcategorias(token)
    return render(request,'subcategorias.html',{'subcategorias':subcategorias})
@validar_token_
def actualizarSubcategoria(request, id):
    token = request.session['token']
    subcategoria = get_subcategoria(id, token)
    categorias = get_categorias(token)
    if request.method == 'POST':
        print('categoria:',request.POST.get("categoria"))
        if 'img' in request.FILES:
            subcategoria = {
                "subcategoria":request.POST.get("subcategoria"), 
                "categoria":request.POST.get("categoria"), 
                "descripcion": request.POST.get("descripcion"),
                "img":request.POST.get("base64"),
            }
        else: 
            subcategoria = {
                "subcategoria":request.POST.get("subcategoria"),
                "categoria":request.POST.get("categoria"), 
                "descripcion": request.POST.get("descripcion")
            }
        actualizar_subcategoria(id, subcategoria, token)
        return redirect('/Subcategorias/')
    return render(request,'operacionesSubcategoria.html',{'subcategoria':subcategoria,'operacion':'Actualizar','categorias':categorias})
@validar_token
def registrarSubcategoria(request):
    token = request.session['token']
    categorias = get_categorias(token)
    if request.method == 'POST' and 'img' in request.FILES:
        subcategoria = {
            "subcategoria":request.POST.get("subcategoria"),
            "categoria":request.POST.get("categoria"),
            "descripcion": request.POST.get("descripcion"),
            "img":request.POST.get("base64"),
            }
        registrar_subcategoria(subcategoria, token)
        return redirect('/Subcategorias/')
    return render(request,'operacionesSubcategoria.html',{'operacion':'Registrar','categorias':categorias})

@validar_token_
def eliminarSubcategoria(request, id):
    token = request.session['token']
    eliminar_subcategoria(id, token)
    return redirect('/Subcategorias/')

# def select(request):
#     categorias = get_categorias()
#     subcategorias = get_subcategoriasID()
#     cadenatemp = ""
#     cadena = ""
#     contadorCat = 0
#     contadorSubcat = 0
#     for c in categorias:
#         cadenatemp = ""
#         contadorCat+=1
#         for s in subcategorias:
#             contadorSubcat += 1
#             if c["id"] == s["categoria"]:
#                 if contadorSubcat == len(subcategorias):
#                     cadenatemp += s["subcategoria"]
#                 else:
#                     cadenatemp += s["subcategoria"] + ","
#         if contadorCat == len(categorias):
#             if len(cadenatemp) > 0:
#                 cadena += str(c["id"]) + ":" + cadenatemp
#         else:
#             if len(cadenatemp) > 0:
#                 cadena += str(c["id"]) + ":" + cadenatemp + "-"

#     return render(request,'select.html',{'categorias':categorias,'subcategorias':cadena})
