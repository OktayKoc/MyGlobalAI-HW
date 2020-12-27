sayac = 1
degerler = list()
while (sayac < 6):
    gecici = input("Please write your {}. value: ".format(sayac))
    degerler.append(gecici)
    sayac += 1
sayac = 1
for i in degerler:
    print("Your {}. value is {} and its value type is : {}".format(sayac, i,type(i)))
    sayac += 1
