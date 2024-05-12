from django.shortcuts import render
import numpy as np

def calcular_raizes(request):
    if request.method == "POST":
        a = float(request.POST.get('a'))
        b = float(request.POST.get('b'))
        c = float(request.POST.get('c'))
        delta = b**2 - 4*a*c
        if delta > 0:
            x1 = (-b + np.sqrt(delta)) / (2 * a)
            x2 = (-b - np.sqrt(delta)) / (2 * a)
            resultado = f"Duas raízes reais: {x1} e {x2}"
        elif delta == 0:
            x = -b / (2 * a)
            resultado = f"Uma raiz real: {x}"
        else:
            resultado = "Sem raízes reais."
        return render(request, 'calculadora/resultado.html', {'resultado': resultado})
    return render(request, 'calculadora/index.html')


def home(request):
    return render(request, 'calculadora/home.html')