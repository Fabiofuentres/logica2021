
# datos basicos nombre , apellido,edad,sexo,peso ,estatura,e-mail.
# solicitar datos al usuario y validar datos.

print ("ingresar Nombre y apellido")
Nombre = input()
if Nombre == "":
    print("ingrese nombre")
print("Ingrese su edad")
Edad = input()
if Edad =="":
    print ("debe ingresar dato")
sexu = input("ingrese sexo F=femenino M= masculino O= otros")
if sexu == "M":
    print("Masculino")
elif sexu == "F":
    print("Femenino")
elif sexu == "O":
    print ("Persona desconocida")
else:
    print ("no identificado")

peso = input("ingrese peso ")
if peso == "":
    print("ingrese dato")
Estatura = input ("ingresar estatura en cms")
if Estatura =="":
    print("ingrese estatura en cms")
Email = input ("ingresar e-mail") 
if Email =="":
    print("ingrese correo")
print("Su nombre es",Nombre,"su edad es",Edad,"su sexo es",sexu,"su peso es",peso,"su estatura es",Estatura," su email es",Email )