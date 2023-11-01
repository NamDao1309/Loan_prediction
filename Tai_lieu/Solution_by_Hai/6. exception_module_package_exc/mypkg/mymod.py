# mymod.py
# a) Write a function countLines(name) that reads an input file and counts the number of lines in it.
def countLines(name):
    with open(name, 'r') as file:
        lines = file.readlines()
        return len(lines)

# b) Write a function countChars(name) which reads an input file and counts the number of characters in it.
def countChars(name):
    with open(name, 'r') as file:
        content = file.read()
        return len(content)

# c) Write a program that asks the user for a file name and calls the above functions to print the number of lines and characters in the file.
def test(name):
    lines = countLines(name)
    chars = countChars(name)
    print(f"Number of lines: {lines}")
    print(f"Number of characters: {chars}")

# 3. __main__

if __name__ == "__main__":
    test('D:\Coding\Python\exception_module_package_exc\data_for_mymod.txt')