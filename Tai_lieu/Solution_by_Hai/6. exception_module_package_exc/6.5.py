import os
import random

# Select a random element from a list
my_list = [1, 2, 3, 4, 5]
random_list_element = random.choice(my_list)

# Select a random element from a set
my_set = {1, 2, 3, 4, 5}
random_set_element = random.choice(list(my_set))

# Select a random value from a dictionary
my_dict = {"a": 1, "b": 2, "c": 3}
random_dict_value = random.choice(list(my_dict.values()))

# Select a random file from a directory
directory_path = "/"
random_file = random.choice(os.listdir(directory_path))

print(f"Random element from list: {random_list_element}")
print(f"Random element from set: {random_set_element}")
print(f"Random value from dictionary: {random_dict_value}")
print(f"Random file from directory: {random_file}")
