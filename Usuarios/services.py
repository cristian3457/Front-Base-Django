import requests
from EjemploFront.settings import URL_SERVER
def iniciar_sesion(usuario, password):
    usuario = {
        "usuario": usuario,
        "password": password
    }
    response = requests.post(URL_SERVER+'usuarios/login/', usuario)
    return response
def get_token(token):
    headers = {
        'Authorization':'token ' + token
    }
    return headers

def valida_token(datos):
    response = requests.post(URL_SERVER+'usuarios/validaToken/', datos)
    return response.json()

def actualizarPassword(id,usuario, password, token):
    
    usuario = {
        "username": usuario,
        "password": password
    }
    response = requests.put(URL_SERVER+'usuarios/usuario/'+str(id)+'/', usuario, headers=get_token(token))
    print(response.status_code)
    if( response.status_code == 200 ):
        return True
    else:
        return False
