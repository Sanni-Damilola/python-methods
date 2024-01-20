# String Formatting

name = "John"
print("Hello, %s!" % name)

name =  "Anu"
age = 10
print("%s is %d years old." % (name, age))

myList = [1,2,3]
print("A list: %s:" % myList)

# %s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - Floating point numbers

# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

# %x/%X - Integers in hex representation (lowercase/uppercase)

# greetings = "Hello"
# name = "John Doe"
# balance = 53.44

# print("%s %s. Your Current Balance is: %d" % (greetings, name, balance))

# first_name = "John"
# last_name = "Doe"
# balance = 53.44

# output_string = "Hello {}. {}. Your current balance is ${:.2f}.".format(first_name, last_name, balance)

# print(output_string)


data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%.2f."

print(format_string % data)
