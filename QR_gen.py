import qrcode

na_chto = input('На что куракод ')

version = int(input('размер поля '))
box_size = int(input('сложность куракода, не больше 3 '))

qr = qrcode.QRCode(version, box_size, border = 5)

qr.add_data(na_chto)

qr.make(fit=True)
img = qr.make_image(fill_color='black', back_color='white')

name = input('Назови меня ')

img.save(f'{name}.png')

print('Куракод создан')
