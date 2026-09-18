# Oppgave 3.1

# def hello():
#     print("Hello World")

# hello()
# hello()
# hello()

# Oppgave 3.3


# global_variable = "I am a global variable"


# def function():
#     global global_variable
#     local_variable = "I am a local variable"
#     global_variable = "I am a global variable modified"
#     return local_variable, global_variable

# def print_variables():
#     print(global_variable)
#     try:
#         print(local_variable)
#     except NameError:
#         print("local_variable is not defined in this scope")

# function()
# print_variables()

#oppgave 3.4

# def function(timesToRun):
#     for i in range(timesToRun):
#         print("Hello World")
# function(3)

# Oppgave 3.5

# def hourlyWage(hoursWorked, hourlyRate):
#     return hoursWorked * hourlyRate


# print("You have earned: ", (hourlyWage(int(input("Hours worked: ")), int(input("Hourly rate: ")))))

# Oppgave 3.6

# def averageAge(people):
#     total_age = 0
#     for i in range(people):
#         age = int(input("Skriv inn alder: "))
#         total_age += age
#     return total_age / people

# print(averageAge(int(input("Hvor mange personer er det?:"))))

# Oppgave 3.7

# text = input("Skriv inn tekst: ")
# if any(letter in text for letter in "æøå"):
#     print("JA")
# else:
#     print("NEI")

# Oppgave 3.8

# def stringIndex(index, string):
#     print(string[index])

# stringIndex(int(input("Skriv inn index: ")), input("Skriv inn tekst: "))

# Oppgave 3.9

# def nameFunction(name, lastName):
#     fullname = name + " " + lastName
#     return fullname

# fullname = nameFunction(input("Skriv inn fornavn: "), input("Skriv inn etternavn: "))
# print(fullname)

# Oppgave 3.10

# def function(name):
#     print(f"Hei {name}. Alder og Bosted?")
#     age = input("Skriv inn alder: ")
#     location = input("Skriv inn bosted: ")
#     return age, location

# age, location = function(input("Skriv inn navn: "))
# print(age, location)

#Oppgave 3.11


# def math_function(first_number, second_number, operation):
#     if operation == "/":
#         return first_number / second_number
#     elif operation == "*":
#         return first_number * second_number
#     elif operation == "//":
#         return first_number // second_number
#     elif operation == "%":
#         return first_number % second_number
#     else:
#         return "Invalid operation"

# print(math_function(int(input("Skriv inn første nummer: ")), int(input("Skriv inn andre nummer: ")), input("Skriv inn operasjon: ")))

#Oppgave 3.12

# def findVocal():
#     text = input("Skriv inn tekst: ")
#     for letter in text:
#         if letter in "aeiouyæøå":
#             print(f"Første vokal er: {letter}")
#             return letter
#     print("Ingen vokaler funnet")
#     return None

# print(findVocal())

#Oppgave 3.13

# def functionTwo(action):
#     if action == "1":
#         wageInput = int(input("Skriv inn timelønn: "))
#         return wageInput
#     elif action == "2":
#         hoursInput = int(input("Skriv inn antall timer: "))
#         return hoursInput
#     return None


# def functionOne(hours, wage_per_hour):
#     return hours * wage_per_hour

# print(functionOne(functionTwo("1"), functionTwo("2")))


#Oppgave 3.14

# import random, time
# player1_score = 0
# player2_score = 0
# isRunning = True

# def info():
#     print("Dette er et enkelt tærningsspill med 2 spillere. Hver spiller kaster en terning, og den med høyest tall vinner. Hvis begge får samme tall, blir det uavgjort.")

# def collect_input():
#     player1 = input("Skriv inn navn på spiller 1: ")
#     player2 = input("Skriv inn navn på spiller 2: ")
#     return player1, player2

# def roll_dice():
#     return random.randint(1, 6)

# def game_loop(player1, player2):
#     global player1_score, player2_score
#     print(f"{player1} kaster terningen...")
#     time.sleep(1)
#     player1_roll = roll_dice()
#     print(f"{player1} fikk: {player1_roll}")
#     time.sleep(1)

#     print(f"{player2} kaster terningen...")
#     time.sleep(1)
#     player2_roll = roll_dice()
#     print(f"{player2} fikk: {player2_roll}")


#     if player1_roll > player2_roll:
#         time.sleep(1)
#         print(f"{player1} vinner!")
#         player1_score += 1
#     elif player2_roll > player1_roll:
#         time.sleep(1)
#         print(f"{player2} vinner!")
#         player2_score += 1
#     else:
#         time.sleep(1)
#         print("Det ble uavgjort!")

# def player_score(player1, player2):
#     global player1_score, player2_score
#     print(f"Score: {player1}: {player1_score}, {player2}: {player2_score}")

# def start_game():
#     global isRunning
#     while isRunning:
#         game_loop(player1, player2)
#         player_score(player1, player2)
#         choice = input("Vil du spille igjen? (ja/nei): ")
#         if choice.lower() != "ja":
#             isRunning = False
#             print("Takk for at du spilte!")

# info()
# player1, player2 = collect_input()
# start_game()


#4.1