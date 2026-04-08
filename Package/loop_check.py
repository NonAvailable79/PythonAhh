for i in range(90):
    if i % 9 == 0:
        print('\nSkipping')
        continue
    if i % 25 == 0:
        print('Not doing anything special')
        pass
    if i == 87:
        print('Breaking out')
        break
    else:
        print('Looping at' , i)
        for j in range(5):
            if i == 34 and j == 3:
                print('Breaking j at 3\n')
                break

            print('j is' , j, end='\')
