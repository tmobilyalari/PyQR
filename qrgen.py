import qrcode
import qrcode.image.svg
qr = qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=32,
    border=4,
)
print("Hello User! Please Write Inputs to QR Generator")
qr.add_data(input())
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
type(img)
img.save("png1.png")
img.save("jpg1.jpg")
factory = qrcode.image.svg.SvgImage
factory = qrcode.image.svg.SvgFragmentImage
factory = qrcode.image.svg.SvgPathImage
img = qr.make_image(fill_color="black", back_color="white", image_factory=factory)
type(img)
img.save("svg1.svg")
