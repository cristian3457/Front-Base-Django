import requests
def iniciar_sesion(usuario, password):
    usuario = {
        "usuario": usuario,
        "password": password
    }
    response = requests.post('http://127.0.0.1:7000/usuarios/login/', usuario)
    return response
def get_token(token):
    headers = {
        'Authorization':'token ' + token
    }
    return headers
  
def actualizarPassword(id,usuario, password, token):
    
    usuario = {
        "username": usuario,
        "password": password
    }
    response = requests.put('http://127.0.0.1:7000/usuarios/usuario/'+str(id)+'/', usuario, headers=get_token(token))
    print(response.status_code)
    if( response.status_code == 200 ):
        return True
    else:
        return False
