def findounces(kg, g):
    kilograms = (g + 1000 * kg) / 1000
    ounces = kilograms * 2.2046 * 16

    stone = ounces // (14 * 16)
    ounces = ounces % (14 * 16)
    pounds = ounces // 16
    ounces = ounces % 16

    time.sleep(1)
    result = str(kg) + ' kilograms and ' + str(g) + 'grams is equivalent to ' + str(stone) + ' stones, '+\
                  str(pounds) + ' pounds, and about ' + str(round(ounces, 5)) + ' ounces.'
    return result

def sums():
    is_4_doing = True
    integer_sum = 0
    float_sum = 0.0

    while is_4_doing:
        number = input('Enter an integer or a float. 0 to stop.\n')
        if number == '0':
            is_4_doing = False
        else:
            if '.' in number:
                float_sum += float(number)
            else:
                integer_sum += int(number)

    print('Done!')
    print('Integer sum:', integer_sum, '\n Float sum:', float_sum)


def get_grades(subject1, subject2):
    #since this was copied, the variables are named such
    art = input(subject1 + 'grade: ')        
    sci = input(subject2 + 'grade: ')

    if art == 'd' and sci == 'd': #first failing grade
        result = 'Not promoted'
    elif art == 'f' or sci == 'f':
        if art == 'b' or art == 'a' or sci == 'a' or sci == 'b':
            if art == 'f':
                result = 'Science'
            elif sci == 'f':
                result = 'Art'
        else:
            result = 'Not promoted' # if one fails, the other is worse than 'c'?
    elif art == sci:
        result = 'Choose'
    elif sci == 'a':
        result = subject2 # cannot be the same
    elif sci == 'b' and not art == 'a':
        result = subject2 #cannot be the same
    elif art == 'a':
        result = subject1
    elif art == 'b' and not sci == 'a':
        result = subject1 #cannot be the same
    elif art == 'c':
        result = subject1 # cannot be the same, science was covered, cannot be failing
    elif sci == 'c':
        result = subject2 # 167
    else:
        print('You dummy entered weird things and now you have to try the question again')
        result = 'Youre dum'

    time.sleep(1)
    print('Your result: ', result)

def commafy(anint):
    num = anint
    numstr = ''

    while num > 0:
        if num // 1000 > 0:
            last3 = str(num % 1000).zfill(3)
        else:
            last3 = str(num % 1000)
        num = num // 1000
        if numstr != '':
            numstr = last3 + ',' + numstr
        else:
            numstr = last3 + numstr

    time.sleep(1)
    return numstr

def triangle(rows, start):
    num = start

    for i in range(rows):
        print('   ' * ((rows - i) * 2), end='') # leading spaces for my right justified triangle
        for j in range(i * 2 + 1):
            print(num, end=' ')
            num += 2
        print()=
