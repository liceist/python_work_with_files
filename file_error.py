try:
    f = open('1example_text.txt')
except:
    print("Error opening file")
else:
    f.close()
    print('(Очистка: Зачинення файлу)')
