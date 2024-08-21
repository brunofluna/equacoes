import math

# funções de menu
def mostrar_menu():
    print('1 - Calcular equação do 1º grau.')
    print('2 - Calcular equação do 2º grau.')
    print('3 - Sair do programa.')

# equação do 2º grau
    # usuário informa a, b, e c para chegar ao resultado de x
def calcular_grau_2(a, b, c):
    delta = (b**2)-(4*a*c)
    if delta < 0:
        return "A equação não possui raízes reais."
    elif delta == 0:
        return f'Valor de x é {(-b)/(2*a)}.'
    else:
        raiz_delta = math.sqrt(delta)
        x1 = (-b + raiz_delta)/(2*a)
        x2 = (-b - raiz_delta)/(2*a)
        yield f'Valor de x1: {x1}.'
        yield f'Valor de x2: {x2}.'
    
        
# equação do 1º grau
calcular_grau_1 = lambda a,b: -b/a

    
