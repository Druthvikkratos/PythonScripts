import qrcode # type: ignore

def createQrCode(data, filePath):
    qr = qrcode.QRCode(version=3, box_size=20, border=10)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color= "black", black_color="white")
    img.save(filePath)

createQrCode("Druthvik", 'qrcode.png')