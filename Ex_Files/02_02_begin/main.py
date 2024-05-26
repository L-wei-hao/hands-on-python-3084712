greet = "Hello World"
extened_grt = "Hello World, " + "this is a long string"

name = "John"

interuption = f'Hello {name}'  #f string

greet_format = 'Hello {}'      #template for formatting
formatted = greet_format.format(name)

print(interuption,formatted)

print(formatted.upper())
print(formatted.lower())
print(formatted.replace('John','weihao'))