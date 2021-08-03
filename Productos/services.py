import requests
from EjemploFront.settings import URL_SERVER

def generate_request(url, headers=""):
    response = requests.get(url, headers = headers)
    if response.status_code == 200:
        return response.json()

def get_productos(token):
    headers = get_token(token)
    response = generate_request(URL_SERVER+'productos/producto/', headers= headers)
    if response:
        productos = response
        return productos
    return ''

def get_producto(id, token):
    headers = get_token(token)
    response = generate_request(URL_SERVER+'productos/producto/'+str(id), headers= headers)
    if response:
        producto = response
        return producto
    return ''

def get_categorias(token):
    headers = get_token(token)
    response = generate_request(URL_SERVER+'categorias/categoria/',headers= headers)
    if response:
        categorias = response
        return categorias
    return ''

def get_categoria(id,token):
    headers = get_token(token)
    response = generate_request(URL_SERVER+'categorias/categoria/'+str(id),headers= headers)
    if response:
        categoria = response
        return categoria
    return ''

def get_subcategorias(token):
    headers = get_token(token)
    response = generate_request(URL_SERVER+'subcategorias/subcategoria/',headers= headers)
    if response:
        subcategorias = response
        subcat = []
        # print('cat:',subcategorias[0]['categoria'])
        for cat in subcategorias:
            categoria = get_categoria(cat['categoria'], token)
            cat['categoria'] = categoria['categoria']
            subcat.append(cat)
        return subcat
    return ''

def get_subcategoriasID(token):
    headers = get_token(token)
    response = generate_request(URL_SERVER+'subcategorias/subcategoria/',headers= headers)
    if response:
        subcategorias = response
        return subcategorias
    return ''

def get_subcategoria(id, token):
    headers = get_token(token)
    response = generate_request(URL_SERVER+'subcategorias/subcategoria/'+str(id),headers= headers)
    if response:
        subcategoria = response
        return subcategoria
    return ''

def get_token(token):
    headers = {
        'Authorization':'token ' + token
    }
    return headers

def registrar_producto(producto, token):
    headers = get_token(token)
    response = requests.post(URL_SERVER+'productos/producto/', producto,headers= headers)
    if response:
        producto = response
        return producto
    return '' 

def actualizar_producto(id,producto, token):
    headers = get_token(token)
    response = requests.put(URL_SERVER+'productos/producto/'+str(id)+'/', producto, headers= headers)
    if response:
        producto = response
        return producto
    return '' 

def registrar_categoria(categoria, token):
    headers = get_token(token)
    response = requests.post(URL_SERVER+'categorias/categoria/', categoria, headers= headers)
    if response:
        categoria = response
        return categoria
    return '' 

def actualizar_categoria(id,categoria, token):
    headers = get_token(token)
    response = requests.put(URL_SERVER+'categorias/categoria/'+str(id)+'/', categoria, headers= headers)
    if response:
        categoria = response
        return categoria
    return '' 

def registrar_subcategoria(subcategoria, token):
    headers = get_token(token)
    response = requests.post(URL_SERVER+'subcategorias/subcategoria/', subcategoria, headers= headers)
    if response:
        subcategoria = response
        return subcategoria
    return '' 

def actualizar_subcategoria(id,subcategoria, token):
    headers = get_token(token)
    response = requests.put(URL_SERVER+'subcategorias/subcategoria/'+str(id)+'/', subcategoria, headers= headers)
    if response:
        subcategoria = response
        return subcategoria
    return '' 

def eliminar_producto(id, token):
    headers = get_token(token)
    url = URL_SERVER+'productos/producto/'+str(id)
    response = requests.delete(url, headers= headers)
    if response:
        print('eliminar:',response)
        producto = response
        return producto
    return ''

def eliminar_categoria(id, token):
    headers = get_token(token)
    url = URL_SERVER+'categorias/categoria/'+str(id)
    response = requests.delete(url, headers= headers)
    if response:
        categoria = response
        return categoria
    return ''

def eliminar_subcategoria(id, token):
    headers = get_token(token)
    url = URL_SERVER+'subcategorias/subcategoria/'+str(id)
    response = requests.delete(url, headers= headers)
    if response:
        subcategoria = response
        return subcategoria
    return ''

