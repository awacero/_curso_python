

from classejm1 import Employee

lista=['A', 'B', 'C','D' ,'E']

for i,e in  enumerate( lista):
    emp1 = Employee(e, i*1000)

print ("Total Employee %d" % Employee.empCount)

emp1.displayCount()

emp1.displayEmployee()

emp1.display_all_employee()

