from django.shortcuts import render, redirect
from .services import iniciar_sesion
# Create your views here.

def iniciarSesion(request):
    if request.method == "POST":
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
        respuesta = iniciar_sesion(usuario,password)
        print('respuesta:',respuesta)
        respuesta = respuesta.json()
        if respuesta['response']:
            request.session['usuario'] = respuesta['data']
            request.session['token'] = respuesta['token']
            print("token:",request.session['token'])
            return redirect("/home")
        else:
            return redirect("/?novalido")
    return render(request,'login.html')

def logout(request):
    request.session['usuario'] = ""
    return redirect('/')