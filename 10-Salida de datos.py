nombre="Gustavo"
edad=28
texto="viejo choto"
bool=True

print("El es",nombre,", tiene",edad,"años,","¿el es un",texto,"?")              #Una forma de salida de datos
print(bool)
print(type(bool))
print("\n") #Con \n se hace un salto de linea

print('Me llamo {} y tengo {} años, ¿Soy un {} ?'.format(nombre,edad,texto))    #Con la funcion format se facilita la
print(not(bool))                                                                #salida de datos
print(type(bool))
print("\n")

print(f"Repito, mi nombre es {nombre}, tengo {edad} años y no soy un {texto}")  #Con la funcion f se hace mas facil la
print(bool)                                                                     #salida de datos, y es las mas usada