'''
Prioridad para operaciones aritmeticas:
1-Parentesis: ()
2-Exponenciacion: **
3-Multiplicacion, division y modulo: * , / , %
4-Suma y resta: + , -
'''
num1=139
num2=13
num3=2
num4=6
suma=num1+num2
resta=num1-num2
producto=num1*num2
division= num1/num2
resto=num1%num2 #Con el simbolo % el resultado es el resto de una division
potencia=num3**num4 #Con el simbolo ** el num3 se eleva al num4
resultado=(3**3)*(13/5-(2*4))

print(suma)
print(resta)
print(producto)
print(division)
division= num1 // num2 #Aca se realiza la division y python muestra un resultado entero redondeado hacia abajo
print(division)
print(resto)
print(potencia)
print(resultado)