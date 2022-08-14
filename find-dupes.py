# Python code to demonstrate
# finding duplicate values from a dictionary

# initialising dictionary
import json

file_name = '2023-league.json'
with open(file_name) as _f:
    ini_dict = json.load(_f)

# printing initial_dictionary
# print("initial_dictionary", str(ini_dict))

# finding duplicate values
# from dictionary
# using a naive approach
rev_dict = {}

for key, value in ini_dict.items():
    rev_dict.setdefault(value, set()).add(key)

result = [key for key, values in rev_dict.items()
          if len(values) > 1]

# printing result
print("duplicate values", str(result))
