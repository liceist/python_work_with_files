try:
    with open('example_text.txt', 'r') as file:
        contents = file.read()
except:
    print ("Error opening file")
