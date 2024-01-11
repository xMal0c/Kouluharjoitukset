def Kertoma(n, kierros = 1):
    if kierros > n:
        return 1
    tulos = 1
    tulos *= kierros

    return tulos * Kertoma(n, kierros + 1)

print(Kertoma(5))

# 6! = 6 * 5 * 4 * 3 * 2 * 1

#0! = 1
#1! = 1
#2! = 2
#3! = 6

#Kertoma(5)
#Kertoma(5,3)
#Kertoma(5, kierros = 2)