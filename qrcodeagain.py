import qrcode

def generate_qr_code(text):
    # Create a QR code instance
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    # Add the data to the QR code
    qr.add_data(text)
    # Generate the QR code
    qr.make(fit=True)
    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    # Save the image
    img.save("qr_code.png")

# Generate a QR code for the text "Hello, World!"
generate_qr_code("Ramesh Sapkota")
