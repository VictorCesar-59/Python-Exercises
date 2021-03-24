from time import sleep
for c in range(1, 11):
    print(f'\033[31m{c}')
    sleep(1)
print('\033[33mOlá mundo!!!')
