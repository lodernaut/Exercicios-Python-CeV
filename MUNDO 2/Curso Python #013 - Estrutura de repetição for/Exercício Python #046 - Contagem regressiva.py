from time import sleep
print('Contagem Regressiva')
for c in range(10, 0, -1):
    print(f'\033[35m{c}\033[m')
    sleep(1)
print('BOOOm!!!') 
