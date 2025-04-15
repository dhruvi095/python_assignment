import qrcode

# Get data from user
data = input("Enter the text or URL to generate QR code: ")

# Create QR code
qr = qrcode.QRCode(
    version=1,  # Controls size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
    box_size=10,
    border=4
)

qr.add_data(data)
qr.make(fit=True)

# Create an image
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("qr_code.png")
print("✅ QR code saved as 'qr_code.png'")
