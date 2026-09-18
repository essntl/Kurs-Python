
#Oppgave 1.7
iterations:int = 1
values:list = []
number = int(input("Skriv nummer: "))
values.append(number)
# 1 - Addition | 2 - Subtraction | 3 Multiplication | 4 Division

for i in range(iterations):
    operation = int(input("Hva vil du gjøre? 1+, 2-, 3*, 4/: "))
    number = int(input("Skriv nummer: "))
    values.append(number)
    if operation == 1: 
        print(values[0] + values[1]);result = values[0] + values[1]; values = [result]
    elif operation == 2:
        print(values[0] - values[1]);result = values[0] - values[1]; values = [result]
    elif operation == 3:
        print(values[0] * values[1]);result = values[0] * values[1]; values = [result]
    elif operation == 4:
        print(values[0] / values[1]);result = values[0] / values[1]; values = [result]
    else:
        print("Invalid operation, try again")
        break
    choice = input("Vil du legge til mer? 1 - Ja, 0 - Nei: ")
    if choice != "1" and choice != "Ja":
        break
    else:
        iterations += 1
        print(iterations)
    
