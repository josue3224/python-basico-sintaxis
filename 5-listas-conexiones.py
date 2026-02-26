#josue gabriel
#listas
lista = ["josue","gabriel",25,True]
print(lista[0])

#lista de frutas.
frutas = ["Naranja","platano","manzana","palta"]
print(frutas[1])
for i in frutas:
    print(i)

#matriz
matriz = [
    [1,2,3],
    [4,6,1],
    [0,1,0],
]
print(matriz[2][2])

#lista de numeros 

numeros = [1,2,3,4,5,6,7,8,9]
print(numeros[8])
print(numeros[:3])
print(numeros[1:5])
print(numeros[1:5])
print(numeros[::2])
print(numeros[::-1])

#ciclo for en la lista
for i in numeros:
    print(i*10)
    
#metodos en las listas
print("---------------------------metodos")
frutas = ["Naranja","platano","manzana","palta"]

#agregar un nuevo dato

frutas .append("ciruela")
print(frutas)

#insert
frutas.insert(2,"Pera")
print(frutas)

#remove = borrar un dato
frutas.remover("platano")
print(frutas)

#pop = para obtener o eliminar el ultimo dato
frutas.popo()
print(frutas)

#sort() ordenar las lista
frutas.reverse()
print(frutas)

#reverse() = revertir
frutas.reverse()
print(frutas)

#len() contar datos
cantidad = len(frutas)
print(cantidad)

#


