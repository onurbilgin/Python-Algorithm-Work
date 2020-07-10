
#Soru 1
o = {1: "Ocak", 2: 'Şubat', 3: 'Mart', 4: 'Nisan', 5: 'Mayıs', 6: 'Haziran',  7: "Temmuz", 8: 'Ağustos', 9: 'Eylül', 10: 'Ekim', 11: 'Kasım', 12: 'Aralık'}
n = int(input("Gün Giriniz: "))
u = int(input("Ay Giriniz: "))
r = int(input("Yıl Giriniz: "))
print("Cevap: ", n, o[u], r)

#Soru 2
from functools import reduce
o = []
n = int(input("1-16 Arasında Bir Sayı Giriniz: "))
if (9 <= n <16):
    for u in range(2, (n*2)+1, 2):
        o.append(u)
    print("Fonksiyonun Sonucu:", reduce(lambda r, b: r+b, o))
elif(9 > n >= 0):
    if (n == 0):
        print(1)
    else:
        for u in range(1, n+1):
            o.append(u)
    print("Fonksiyonun Sonucu:", reduce(lambda r, b: r*b, o)*3)
else:
    print("Girdiğiniz Sayı 15'den Büyük veya Negatif Bir Sayıdır! ")
    
#Soru 3
o = {"o": 15, "n": 14, "u": 21, "r": 18, "b": 2, "i": 9, "l": 12, "g": 7, "i": 9, "n": 14, "o": 15, "n": 14}
n = [[1, 2, -1], [2, 5, 2], [-1, -2, 2]]
def sifre(adsoyad):
    u = []
    for r in adsoyad:
        u.append(r)
   
    b = []
    for r2 in adsoyad:
        b.append(o.get(r2))
    
    onur = b[0:3]
    onur1 = b[3:6]
    onur2 = b[6:9]
    onur3 = b[9:12]
    b2 = [onur, onur1, onur2, onur3]
    print(b2)
    print(n)
    bilgin = []
    for r3 in b2:
        for r4 in n:
            print("İşlem", r4, r3)
            onurbilgin = r4[0] * r3[0], r4[1] * r3[1], r4[2] * r3[2]
            print(onurbilgin)
            onur4 = 0
            for r5 in onurbilgin:
                onur4 += r5
            print(onur4)
            bilgin.append(onur4)
        print("Liste: ", bilgin)
    
islem = sifre("onurbilginon")

#Soru 4
o=[]
for n in range(1,22):
    if n==2 or n==3 or n==5 or n==7:
        o.append(n)
    if not n%2==0 and n!=1 and n%3!=0 and n%5!=0 and n%7!=0:
        o.append(n)

print(o)