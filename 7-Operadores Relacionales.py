'''
Operadores relacionales
>   mayor
<   menor
>=  mayor o igual
<=  menor o igual
!=  distinto
== igual
'''
num1=15
num2=122
num3=45
premisa1=17 < 10
premisa2=13 > 5
resultado= num1*num2 != num3 #En python se da prioridad a los operadores artimeticos y luego a los relacionales
print("La afirmacion 1 es:", premisa1) #Con "," (coma) se separa el texto a imprimir del valor de la variable que
print("La afirmacion 2 es:", premisa2) #tambien se desea imprimir
print("El resultado de la operacion es:", resultado)