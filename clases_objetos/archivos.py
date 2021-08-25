
file = open("./devices.txt",'r')

lista_cisco = []
for i in file:
    i=i.strip()
    print(i)



for i in file:
    i=i.strip()
    print(i)
    lista_cisco.append(i)

file.close()

print(lista_cisco)


