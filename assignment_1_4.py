num = input("Enter the number: ")
try:
    print(10/int(num))
except ZeroDivisionError:
    print("Cannot devide")
