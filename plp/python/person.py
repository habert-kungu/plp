class Person:
    def __init__(self, name, age, gender, education):
        self.name = name
        self.age = age
        self.gender = gender
        self.education = education

    def introduce(self):
        print(
            f"Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender} i'mcurrently pursuing {self.education}."
        )


# Create an instance of the Person class
person1 = Person("Alice", 30, "female", "Masters")

# Call the introduce method to display the person's information
person1.introduce()
