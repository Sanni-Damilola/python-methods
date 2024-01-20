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

greetings = "Hello"
name = "John Doe"
balance = 53.44

print("%s %s. Your Current Balance is: %d" % (greetings, name, balance))