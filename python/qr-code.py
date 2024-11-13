import qrcode
from PIL import Image

# Details of the wedding invitation
invitation_details = "https://arsene-birthday-wishes.netlify.app"

# Create a QR code from the invitation details
qr = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(invitation_details)
qr.make(fit=True)

# Create a QR code image
qr_image = qr.make_image(fill_color="black", back_color="white").convert("RGBA")



# Save the final QR code image
qr_image.save("Birthday_wishes_qr_with_image.png")

print("QR code with image fill generated and saved as 'Birthday_wishes_qr_with_image.png")
