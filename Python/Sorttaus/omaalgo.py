
def Laijttelu(lista):
    for i in range(1, len(lista)):
        vertaus = lista[i]
        j = i - 1

        while j >= 0 and vertaus < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = vertaus


alkulista = [1000, 900, 554, 556, 100, 11, 72, 3]
print("Alkuperäinen lista:", alkulista)

Laijttelu(alkulista)
print("Lajiteltu lista:", alkulista)
