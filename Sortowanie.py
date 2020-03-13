from random import randint

def losowa_lista(n):
    lista=[]
    for i in range(0,n):
        lista.append(randint(0,100))
    print('Losowa lista:')
    print(lista)
    return lista

def posortowana_lista(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
               lista[i], lista[j] = lista[j], lista[i]
    print('Posortowana lista_1:')
    print(lista)
    return lista

def posortowana_lista2(lista):
    for i in range(len(lista)):
        min_lista = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_lista]:
                min_lista = j
        lista[i], lista[min_lista] = lista[min_lista], lista[i]
    print('Posortowana lista_2:')
    print(lista)
    return(lista)

def sortowanie(lista):
    posortowana_lista(lista)
    posortowana_lista2(lista)

    
sortowanie(losowa_lista(n=int(input('Wprowadź ilość liczb: '))))

