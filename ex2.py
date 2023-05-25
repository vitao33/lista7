num = int(input('Informe o número :'))
for i in range( num + 1 ):
    if i % 7 == 0 or i % 3 == 0:
        print('*')
    else:
         print(i)