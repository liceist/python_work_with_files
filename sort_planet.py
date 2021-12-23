try:
    with open('plan.txt', 'r') as file:
        lst = []
        for line in file:
            lst.append(line.split('\n')[0])
        lst.sort()

    with open('sort_plan.txt', 'w') as sort_file:
        sort_file.write('\n'.join(lst))

    print('Success. Planets are sorted')
except:
    print('Something went wrong')
