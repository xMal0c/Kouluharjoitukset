import random

#luodaan lista joka alkaa 1 päättyy n
def LuoLista(n):
    return list(range(1, n + 1))

#oma listan sekotus
def OmaSekoitus(lista):
    for i in range(len(lista)):
        RandomIndex = random.randint(0, len(lista) - 1)
        lista[i], lista[RandomIndex] = lista[RandomIndex], lista[i]

#Bogo sorttaus
def Bogosorttaus(lista):
    while any(lista[i] > lista[i + 1] for i in range(len(lista) - 1)):
        OmaSekoitus(lista)

n = 10
PerusLista = LuoLista(n)
print("Perus lista:", PerusLista)

OmaSekoitus(PerusLista)
print("Sekoitettu lista:", PerusLista)

Bogosorttaus(PerusLista)
print("Järjestetty lista:", PerusLista)
