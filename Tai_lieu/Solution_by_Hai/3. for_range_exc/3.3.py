s = "Bai Tap Mon Lap Trinh Python"
result = ""

i = 0
while i < len(s):
    if s[i] == " ":
        result += "\n"
    else:
        result += s[i]
    i += 1

print(result)
