
try:
    num = int(input("Enter: "))
    print(10 / num)
except ZeroDivisionError:
    print("Do not enter 0")
except ValueError:       
    print("Enter the number please")
