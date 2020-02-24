nombreApellido=input("Ingrese su nombre y apellido: ")  #Asi se ingresa datos de tipo string o cadena de caracteres
edad=int(input("Ingrese su edad: "))                    #Asi se ingresa datos de tipo entero
num=float(input("Ingrese un numero decimal: "))         #Asi se ingresa datos de tipo flotante
print("\n")
print("Sus datos son:")
print(f"Nombre y Apellido: {nombreApellido}")
print(f"Edad: {edad} años")
print(f"El numero decimal ingresado mas 5 es: {num+5}") #Debe ingresar numeros con punto porque con coma falla el programa