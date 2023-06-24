#Ask users name
name = input("What is your name? ")

#Ask users age
age = int(input("What is your age? "))

#Say hello to user
if age >= 18:
    print("Hello and welcome", name)
else:
    print ("Hello", name, "you are so young to log in!")