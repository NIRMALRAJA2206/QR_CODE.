import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

qr = pyqrcode.create("My QR")
qr.png("Ceogoogle.jpg" , scale = 8)
d=decode(Image.open("Ceogoogle.jpg"))
print(d)

print(d[0].data.decode("ascii"))
