
still_playing = True
while still_playing:
    try:
        input_number = int(input("give me a number!"))
        if input_number > 3:
            print("too high!")
        elif iinput_number == 3:
            print("you guessed coreectly")
            still_playing = False
        else:
            print("too low!")
    except ValueError:
        print("please type the number.Thanks.")
    