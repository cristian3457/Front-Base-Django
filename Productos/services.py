import requests

def generate_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()

def get_productos():
    response = generate_request('http://127.0.0.1:7000/productos/producto/')
    if response:
        productos = response
        return productos
    return ''

def get_producto(id):
    response = generate_request('http://127.0.0.1:7000/productos/producto/'+str(id))
    if response:
        producto = response
        return producto
    return ''

def get_categorias():
    response = generate_request('http://127.0.0.1:7000/categorias/categoria/')
    if response:
        categorias = response
        return categorias
    return ''

def get_categoria(id):
    response = generate_request('http://127.0.0.1:7000/categorias/categoria/'+str(id))
    if response:
        categoria = response
        return categoria
    return ''

def get_subcategorias():
    response = generate_request('http://127.0.0.1:7000/subcategorias/subcategoria/')
    if response:
        subcategorias = response
        subcat = []
        # print('cat:',subcategorias[0]['categoria'])
        for cat in subcategorias:
            categoria = get_categoria(cat['categoria'])
            cat['categoria'] = categoria['categoria']
            subcat.append(cat)
        return subcat
    return ''

def get_subcategoriasID():
    response = generate_request('http://127.0.0.1:7000/subcategorias/subcategoria/')
    if response:
        subcategorias = response
        return subcategorias
    return ''

def get_subcategoria(id):
    response = generate_request('http://127.0.0.1:7000/subcategorias/subcategoria/'+str(id))
    if response:
        subcategoria = response
        return subcategoria
    return ''

def registrar_producto(producto):
    response = requests.post('http://127.0.0.1:7000/productos/producto/', producto)
    if response:
        producto = response
        return producto
    return '' 

def actualizar_producto(id,producto):
    response = requests.put('http://127.0.0.1:7000/productos/producto/'+str(id)+'/', producto)
    if response:
        producto = response
        return producto
    return '' 

def registrar_categoria(categoria):
    response = requests.post('http://127.0.0.1:7000/categorias/categoria/', categoria)
    if response:
        categoria = response
        return categoria
    return '' 

def actualizar_categoria(id,categoria):
    response = requests.put('http://127.0.0.1:7000/categorias/categoria/'+str(id)+'/', categoria)
    if response:
        categoria = response
        return categoria
    return '' 

def registrar_subcategoria(subcategoria):
    response = requests.post('http://127.0.0.1:7000/subcategorias/subcategoria/', subcategoria)
    if response:
        subcategoria = response
        return subcategoria
    return '' 

def actualizar_subcategoria(id,subcategoria):
    response = requests.put('http://127.0.0.1:7000/subcategorias/subcategoria/'+str(id)+'/', subcategoria)
    if response:
        subcategoria = response
        return subcategoria
    return '' 

def eliminar_producto(id):
    url = 'http://127.0.0.1:7000/productos/producto/'+str(id)
    response = requests.delete(url)
    if response:
        print('eliminar:',response)
        producto = response
        return producto
    return ''

def eliminar_categoria(id):
    url = 'http://127.0.0.1:7000/categorias/categoria/'+str(id)
    response = requests.delete(url)
    if response:
        categoria = response
        return categoria
    return ''

def eliminar_subcategoria(id):
    url = 'http://127.0.0.1:7000/subcategorias/subcategoria/'+str(id)
    response = requests.delete(url)
    if response:
        subcategoria = response
        return subcategoria
    return ''

