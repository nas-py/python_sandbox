# Variables = A Container for a value. Behaves as the value that it contains

first_name = 'John'
last_name = 'Smith'
full_name = first_name + last_name  # concatenation
print('Hello ' + full_name)
print(type(full_name))  # string

birth_year = 1994
year = 2022
age = year - birth_year
print(type(age))    # int
print('Age: ' + str(age))   # type casting

price = 199.99
print(type(price))
print('price: ' + str(price))

he_has_good_income = False
print(type(he_has_good_income))     # boolean
print('Have good income? ' + str(he_has_good_income))

# Multiple assignment = allows us to assign multiple variables at the same time in
#                       one line of code

name, age, year = 'Bro', 1994, 2021
print(name, age, year)

apple = orange = banana = 19.55
print(apple, orange, banana)
