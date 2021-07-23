from django.shortcuts import redirect, render
from .services import get_subcategoriasID,eliminar_subcategoria, eliminar_categoria, eliminar_producto, get_productos, get_producto, registrar_producto, actualizar_producto, get_categorias, get_subcategorias, registrar_categoria, get_categoria, actualizar_categoria, actualizar_subcategoria, registrar_subcategoria, get_subcategoria


# Create your views here.

def home(request):
    productos = get_productos
    return render(request,'home.html',{'productos':productos})

def actualizar(request, id):
    producto = get_producto(id)
    categorias = get_categorias()
    subcategorias = get_subcategoriasID()
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
        actualizar_producto(id, producto)
        return redirect('/productos/')
    return render(request,'actualizarProducto.html',{'producto':producto,'operacion':'Actualizar', 'categorias':categorias,'subcategorias':cadena})

def registrar(request):
    categorias = get_categorias()
    subcategorias = get_subcategoriasID()
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
        registrar_producto(producto)
        return redirect('/productos/')
    return render(request,'actualizarProducto.html',{'operacion':'Registrar', 'categorias':categorias,'subcategorias':cadena})

def eliminar(request, id):
    eliminar_producto(id)
    return redirect('/productos/')

def productos(request):
    productos = get_productos
    return render(request,'productos.html',{'productos':productos})

def categorias(request):
    categorias = get_categorias
    return render(request,'categorias.html',{'categorias':categorias})

def actualizarCategoria(request, id):
    categoria = get_categoria(id)
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
        actualizar_categoria(id, categoria)
        return redirect('/productos/Categorias/')
    return render(request,'operacionesCategoria.html',{'categoria':categoria,'operacion':'Actualizar'})

def registrarCategoria(request):
    if request.method == 'POST' and 'img' in request.FILES:
        categoria = {
            "categoria":request.POST.get("categoria"),
            "descripcion": request.POST.get("descripcion"),
            "img":request.POST.get("base64"),
            }
        registrar_categoria(categoria)
        return redirect('/productos/Categorias/')
    return render(request,'operacionesCategoria.html',{'operacion':'Registrar'})

def eliminarCategoria(request, id):
    eliminar_categoria(id)
    return redirect('/productos/Categorias/')


def subcategorias(request):
    subcategorias = get_subcategorias
    return render(request,'subcategorias.html',{'subcategorias':subcategorias})

def actualizarSubcategoria(request, id):
    subcategoria = get_subcategoria(id)
    categorias = get_categorias()
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
        actualizar_subcategoria(id, subcategoria)
        return redirect('/productos/Subcategorias/')
    return render(request,'operacionesSubcategoria.html',{'subcategoria':subcategoria,'operacion':'Actualizar','categorias':categorias})

def registrarSubcategoria(request):
    categorias = get_categorias()
    if request.method == 'POST' and 'img' in request.FILES:
        subcategoria = {
            "subcategoria":request.POST.get("subcategoria"),
            "categoria":request.POST.get("categoria"),
            "descripcion": request.POST.get("descripcion"),
            "img":request.POST.get("base64"),
            }
        registrar_subcategoria(subcategoria)
        return redirect('/productos/Subcategorias/')
    return render(request,'operacionesSubcategoria.html',{'operacion':'Registrar','categorias':categorias})


def eliminarSubcategoria(request, id):
    eliminar_subcategoria(id)
    return redirect('/productos/Subcategorias/')

def select(request):
    categorias = get_categorias()
    subcategorias = get_subcategoriasID()
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

    return render(request,'select.html',{'categorias':categorias,'subcategorias':cadena})
