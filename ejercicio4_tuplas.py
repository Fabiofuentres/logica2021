#tuplas
# conjunto de datos, separados por coma, que no pueden ser modificajos
#las tuplas parten del 0
#nombre de la tupla {posicion_elemento}
tupla = (1234,"aeiou",0.19,"qwerty")

print (tupla[2:] )
print (tupla [0]) #1234
print (tupla[1])  #"aeiou"
print (tupla[2]) #0.19
print (tupla[3]) #"qwerty"
print (tupla[1:3])#("eaiou",0.19)
print (tupla[:2]) #(1234,"aeiou")
print (tupla[2:]) #(0.19,"qwerty")


#listas conjuntos de datos , separados por coma , ordenados segun ingreso, todos parten de 0


lista = [1234,"aeiou",0.19,"qwerty",True]

print(lista[2]) #0.19
print(lista[4]) #true
lista[0] = 4321 #reemplazando en la posicion 0

print(lista[-1]) #recorrer de manera inversa
print(lista[1])
lista2 = lista[:] # copia de datos

print(lista) #se mantienen los datos
print(lista2) # es copia de lista

lista2[1] = "12345678" #

print(lista)
print(lista2,"asd")

lista3 = lista # 
lista3[1]= "123456789" #

print(lista)
print(lista3,"aqui voy")