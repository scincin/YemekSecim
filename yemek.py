import random
yemekAdi=""
yemekler=[]
#while yemekAdi != "tamam":
s = int(input('kac seceneginiz var'))
for i in range(s):
    yemekAdi = input("Yemek adi giriniz : ")
    yemekler.append(yemekAdi)
print("Random yemeginiz : ", random.choice(yemekler))
