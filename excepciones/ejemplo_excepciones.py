
print("Inicio")


try: 
    x = int(input("Ingrese un numero: "))
    y = 1/ x
    print(y)

except ZeroDivisionError as e:
    print(str(e))

except ValueError as e:
    print(str(e))

except Exception as e:
    print(str(e))


print("Fin")