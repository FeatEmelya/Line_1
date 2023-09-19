import random

Char = '1234567890qwertyuiopasdfghjklzxcvbnm!@#$%^&*()QWERTYUIOPASDFGHJKLZXCVBNM'


HM = input("Сколько нужно паролей?" + "\n")
Lenght = input("Сколько символов необходимо?" + '\n')
HM = int(HM)
Lenght = int(Lenght)

for n in range(HM):
    password = ''
    for i in range(Lenght):
        password += random.choice(Char) #Попробуем хотя бы с одним для начала
    print(password)

