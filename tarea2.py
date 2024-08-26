#DATA STRUCTURES: MORE ON LIST
list1=['azucar', 'leche', 5+4, 'cafe', 8, '10']
print(list1) #Creamos nuestra lista

list1.append('pasteles')
print(list1) #Agregamos la palabra 'pasteles' a la ultima posicion de nuestra lista

list1.extend('18')
print(list1) #Agregamos 18 como 2 elementos separados de la lista
list1.extend('churro')
print(list1) #Agregamos los caracteres de 'churro' como elementos separados de la lista

list1.insert(1, 7+7)
print(list1) #Agregamos el 7+7=14 a la lista, especificamos el lugar de insercion -#before-

list1.remove('leche')
print(list1) #Aqui eliminamos el str que especificamos entre ()

list1.pop()
print(list1) #Sin especificar borra el ultimo elemento
list1.pop(4)
print(list1) #Aqui especificamos el elemento en orden 4

list1.clear()
print(list1) #Aqui eliminamos todos los elementos de la lista

list2= 'chocolate', '23', 'expresso', 33+22, 'miel', 'expresso'
print(list2) #Aqui creamos una nueva lista

print(list2.index('expresso')) #Buscar el valor 'expresso
print(list2.index('expresso',3)) #Buscar el siguiente 'expresso' despues de la posicion 3

print(list2.count('expresso')) #Cuantas veces aparece la palabra indicada
print(list2.count('miel'))

prime_numbers=[11, 3, 7, 5, 2]
prime_numbers.sort()
print(prime_numbers)
prime_numbers.sort(reverse=True)
print(prime_numbers)

paises=['España', 'Francia', 'Mexico', 'Inglaterra', 'Peru']
print(paises)
paises.sort()
print(paises)
paises.sort(reverse=True)
print(paises)
paises.sort(reverse=False)
print(paises)

list3=[1, 2, 3, 4, 5]
print(list3)
list3.reverse() #Para poner al reves los elementos de la lista
print(list3)

list4=['vainilla', 'fresa', 'chocolate', 'napolitano']
print(list4)
list4.reverse()
print(list4)

list5=[0, 'rosa', 46, 'verde', 6+6, '836']
print(list5)
list5.reverse()
print(list5)
