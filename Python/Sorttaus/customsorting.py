import random

def LuoLista(n):
    return list(range(1, n + 1))

#listan sekotus
def OmaSekoitus(lista):
    for i in range(len(lista)):
        RandomIndex = random.randint(0, len(lista) - 1)
        lista[i], lista[RandomIndex] = lista[RandomIndex], lista[i]

n = 10
PerusLista = LuoLista(n)
print("Perus lista:", PerusLista)


OmaSekoitus(PerusLista)
print("Sekoitettu lista:", PerusLista)
