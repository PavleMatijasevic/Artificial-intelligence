

from traceback import print_tb


print("Hello world!")
print('Hello world!')

a = 5
print(a)
b = 6.1
print(b)
print(int(b))

niska = 'Dobar dan!'
print(niska)

for i in range(5):
    print(i)

#n = input()
#print(n)
#print(float(n))
#

try:
    with open("ulaz.txt", "r") as f:
        print(f.read())
except:
    print("Ne moguce otvoriti fajl/Ne postoji fajl!")

izlaz = "izlaz.txt"


ulaz = open("ulaz.txt", "r")
izlaz = open("izlaz.txt", "w")

izlaz.write(ulaz.read())

ulaz.close()
izlaz.close()

lista = [1, 2, 4, 1, 7, 3, 4, 5]

print(lista)
print(lista.count(3)) # broji koliko trojki ima u listi
n = len(lista)
print(n)

for i in lista:
    print(lista[i])


podlista = lista[3:] 
print(lista)
print(podlista)
podlista = lista[-1]
print(lista)
print(podlista)
podlista = lista[0::2] # svaki drugi
print(lista)
print(podlista)