#  find the position of
#  then add 13 to  it
result = ""
alphabet = list("abcdefghijklmnopqrstuvwxyz")
rotate = 13

letter = "a"
for letrer in sentence:
    try:
        position = alphabet.index(letrer)
        new_position =(position + rotate_by)% 26
        new_letter = alphabet[new_position]
        print(new_letter)
        result =+ new_letter
    except ValueError:
        print
        
