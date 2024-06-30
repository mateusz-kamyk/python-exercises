#!/usr/bin/env python3

import random
import string

lowercase_list = list(string.ascii_lowercase)
uppercase_list = list(string.ascii_uppercase)
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

nr_lowercase = 3
nr_uppercase = 3
nr_numbers = 3

pass_lowercase = []
pass_uppercase = []
pass_numbers = []


for letter in range(0, nr_lowercase): 
    pass_lowercase += random.choice(lowercase_list)

for symbol in range(0, nr_uppercase):
    pass_uppercase += random.choice(uppercase_list)

for number in range(0, nr_numbers):
    pass_numbers += random.choice(numbers)

pass_list = list(pass_lowercase + pass_uppercase + pass_numbers)

random.shuffle(pass_list)

password = ''.join(pass_list)

print("Your created password:\n")
print(password)

