import qrcode

url = input("Enter your URL: ").strip()
fileName = input("Enter your filename: ").strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(fileName)

print(f'QR code saved as {fileName}')