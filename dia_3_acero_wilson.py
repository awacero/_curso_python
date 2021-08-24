
first_name, last_name, location, age = input("ingrese su nombre apellido  ciudad  edad: ").split()
age=int(age)
space = " "

print("Su información es: " + first_name.capitalize()+space+last_name.capitalize()+space+location+space+str(age))

if age <= 13 :
    print("Niño")
elif age >13 and age<21:
    print("adolescente")
elif age >21 and age<65:
    print("adulto")
else:
    print("adulto mayor")