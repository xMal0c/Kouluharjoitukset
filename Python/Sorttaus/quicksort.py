
def QuickSort(L):
    if len(L) <= 1:
        return L
    else:
        pivot = L[0]

        #Jaetaan luvut pienempiin ja isompiin
        pienempi = [x for x in L[1:] if x < pivot]
        isompi = [x for x in L[1:] if x > pivot]

        pienempiLista = QuickSort(pienempi)
        suurempiLista = QuickSort(isompi)

        #Palautetaan pienempi + pivot + suurempi
        return pienempiLista + [pivot] + suurempiLista



lista = [8, 3, 7, 4, 1, 6, 9, 2, 5]
järjestettyLista = QuickSort(lista)
print("Järjestetty lista:", järjestettyLista)
