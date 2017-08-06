import random
yemekAdi=""
yemekler=[]
s = int(input('kac seceneginiz var'))
for i in range(s):
    yemekAdi = input("Yemek adi giriniz : ")
    yemekler.append(yemekAdi)
print("Bugunkü Yemeğiniz : ", random.choice(yemekler))
