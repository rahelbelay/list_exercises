
input_number = input("give me a number!")
input_number = int(input_number)
print(input_number)

if input_number > 3:
    print("too high!")
elif input_number == 3:
    print("you guessed coreectly")
else:
    print("too low!")