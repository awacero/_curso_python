min = -20
max = 20

def read_int(aviso,min,max):

    
    while (True):
        try:
            input_value = int(input(aviso))
            assert input_value >= min and input_value <=max
                
            return input_value
            
        except ValueError:
            print("Error en el ingreso")
        except:
            print("Error el valor no esta en el rango")


v = read_int("ingrese un valor entre %s y %s: " %(min,max),min,max)

print(v)