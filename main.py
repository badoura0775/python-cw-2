my_name = input("Enter your user name :")
my_age=int(input("what is your age?"))
print(f"my name is {my_name} and I am {my_age} years old")
firstNumber=int(input("first number: "))
secoundNumber=int(input("secound number: "))
operation=input("select operation")
if operation=="*":
    print(firstNumber*secoundNumber)
elif operation=="/":
    print(firstNumber/secoundNumber)
elif operation=="+":
    print(firstNumber+secoundNumber)
elif operation=="-":
    print(firstNumber-secoundNumber)
else:
    print("operation is not valid")
#part there 
bus_capacity=30
people_inbus=int(input("enter the amount of the passengers in the bus:"))
Askers=int(input("enter the amount of people who want to enter the bus:"))
empty_seats = bus_capacity - people_inbus
if empty_seats>Askers:
    print(f"there are emty seats :لا{empty_seats}")
if empty_seats<=Askers:
    print("No emty seats")