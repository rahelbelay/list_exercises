user_name = input("What is your name?")
#  input -need to take it and save it somewhere
#variable names in python has _
#snake case
#java script camelCase
#print("Hello, ")
#print (user_name)
print ("Hello,", user_name, "!")
# String interpolating has three parts
#1 place holder
greeting = "Hello, %s!" % (user_name,)
#print(greeting)
#print("Hello, " + user_name + "!")
greeting = f"Hello, %s! {user_name}!"
print (greeting)