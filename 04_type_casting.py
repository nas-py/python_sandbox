# type casting = convert the data type of value to another data type

integer = 10
decimal = 10.99
string = '10'
no_value = None
value = 'hello'

print(integer, decimal, string, no_value, value)
print(type(integer), type(decimal), type(string), type(no_value), type(value))

number_to_str = str(integer)
decimal_to_int = int(decimal)
string_to_float = float(string)
none_to_bool = bool(no_value)
value_to_bool = bool(value)

print(type(number_to_str), type(decimal_to_int), type(string_to_float), type(none_to_bool),
      type(value_to_bool))
print(number_to_str, decimal_to_int, string_to_float, none_to_bool, value_to_bool)
# 10 10 10.0 False True
