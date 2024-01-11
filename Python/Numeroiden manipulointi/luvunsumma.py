#Kirjoita funktio, joka laskee argumenttina olevan luvun numeroiden summan.

def LuvunSumma(luku):
    lukustr = str(luku)
    summa = 0
    
    for num in lukustr:
        summa += int(num)
    
    return summa

#Esim. tulokset
tulos1 = LuvunSumma(12345)
tulos2 = LuvunSumma(5544)


print("LuvunSumma(123) tulos on: " + str(tulos1))
print("LuvunSumma(123) tulos on: " + str(tulos2))