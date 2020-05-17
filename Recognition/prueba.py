import base64


image = open('/home/felipedev/Descargas/AI Cloud/Cloud-Computing/Recognition/LicPlateImages/2.png', 'rb')  
image_read = image.read()
image_64_encode = base64.encodestring(image_read)
print(image_64_encode)
