import random

#luodaan lista joka alkaa 1 päättyy n
def LuoLista(n):
    return list(range(1, n + 1))

#oma listan sekotus
def OmaSekoitus(lista):
    for i in range(len(lista)):
        RandomIndex = random.randint(0, len(lista) - 1)
        lista[i], lista[RandomIndex] = lista[RandomIndex], lista[i]

# kupla sortti
def BubbleSort(lista):
    #käydään indeixt läpi 
    for i in range(len(lista)):
        # verrataan kaikki listan sisällä olevt elementit ja vaihdetaan niiden paikka
        for j in range(0, len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j] # vaihdetaan paikkaa jos edellinen > seuraava

n = 10
PerusLista = LuoLista(n)
print("Perus lista:", PerusLista)

OmaSekoitus(PerusLista)
print("Sekoitettu lista:", PerusLista)

BubbleSort(PerusLista)
print("Järjestetty lista:", PerusLista)
