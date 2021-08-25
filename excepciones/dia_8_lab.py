


device_file=("./devices.txt")

def insert_device(device_name):
    file = open(device_file,'a')
    file.write("%s\n" %device_name)
    file.close()

def print_file():
    file = open(device_file,'r').readlines()
    for line in reversed(file):
        
        print(line)

while True:
    entrada = input("Ingrese un nuevo dispositivo, exit para salir: ")

    if entrada == 'exit':
        print("All done")
        print_file()
        
        break
    else:
        "llamar a insertar dispositivo"
        insert_device(entrada)