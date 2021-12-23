with open('example_text.txt', 'r') as file:
    contents = file.read(10)
    lines = file.readlines()
    rest = file.read()
print("10:", contents)
print("залишки:", rest)
print(lines)
