import random
import string

# Generate a random color hex
color_hex = ''.join(random.choice(string.hexdigits) for _ in range(6))

# Generate a random alphabetical string
alphabetical_string = ''.join(random.choice(string.ascii_letters) for _ in range(10))

# Generate a random value between two integers (inclusive)
start = 1
end = 10
random_int = random.randint(start, end)

# Generate a random multiple of 7 between 0 and 70
random_multiple_of_7 = random.randint(0, 10) * 7

print(f"Random color hex: #{color_hex}")
print(f"Random alphabetical string: {alphabetical_string}")
print(f"Random integer between {start} and {end}: {random_int}")
print(f"Random multiple of 7 between 0 and 70: {random_multiple_of_7}")
