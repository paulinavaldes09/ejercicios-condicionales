edad = int(input("Ingrese su edad: "))
x = float(input("Ingrese su promedio de notas: "))

if edad >= 18:
    if x >= 4.0:
        print("Puede acceder a la beca")
    else:
        print("Es mayor de edad pero no cumple con el promedio para la beca")
else:
    print("Es menor de edad")