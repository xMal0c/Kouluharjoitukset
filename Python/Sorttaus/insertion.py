import random

#luodaan lista joka alkaa 1 ja päättyy n
def LuoLista(n):
    return list(range(1, n + 1))

#oma listan sekotus
def OmaSekoitus(lista):
    for i in range(len(lista)):
        RandomIndex = random.randint(0, len(lista) - 1)
        lista[i], lista[RandomIndex] = lista[RandomIndex], lista[i]

#Insertion sort
def InsertionSort(lista):
    for i in range(1, len(lista)):
        current_value = lista[i]
        position = i

        #Siirtää isompia oikealle
        while position > 0 and lista[position - 1] > current_value:
            lista[position] = lista[position - 1]
            position = position - 1
        lista[position] = current_value

n = 10
PerusLista = LuoLista(n)
print("Perus lista:", PerusLista)

OmaSekoitus(PerusLista)
print("Sekoitettu lista:", PerusLista)

InsertionSort(PerusLista)
print("Järjestetty:", PerusLista)
