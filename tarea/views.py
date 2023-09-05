from django.shortcuts import render

def sumar(request, uno, dos):
    res = uno + dos
    return render(request, 'tarea/operacion1.html', {'uno': uno, 'dos': dos, 'res': res})

def restar(request, uno, dos):
    res = uno - dos
    return render(request, 'tarea/operacion2.html', {'uno': uno, 'dos': dos, 'res': res})

def multiplicar(request, uno, dos):
    res = uno * dos
    return render(request, 'tarea/operacion3.html', {'uno': uno, 'dos': dos, 'res': res})