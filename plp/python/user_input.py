#Write a program that asks the user for their name, age, and location 
# and then prints
# out a personalized message.
def user():
    name = input("Name: ")
    age = int(input("Age: "))
    loc = input("Please provide location: ")
    
    print(f"hello, {name} of age {age} you live in {loc}")
    
user()