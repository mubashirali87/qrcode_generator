import qrcode

# Create an instance of the QR code generator
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

# Add data to the QR code
data = "Hello, QR code!"
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code as an image file
img.save("qr_code.png")
