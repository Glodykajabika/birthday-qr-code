import qrcode
from PIL import Image

# Details of the wedding invitation
invitation_details = "https://main--titi-wedding.netlify.app/"

# Create a QR code from the invitation details
qr = qrcode.QRCode(
    version=7,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(invitation_details)
qr.make(fit=True)

# Create a QR code image
qr_image = qr.make_image(fill_color="black", back_color="white").convert("RGBA")

# Open the image to use as the fill color
image_fill = Image.open("C:/Users/HP/Desktop/letters/img/img/2ef7a199a4ee6fb7442a94d87487010.jpg")  # Replace with your image path
image_fill = image_fill.resize(qr_image.size, Image.Resampling.LANCZOS)

# Create a new image for the final QR code
final_qr = Image.new("RGBA", qr_image.size)

# Loop through the pixels of the QR code
for x in range(qr_image.size[0]):
    for y in range(qr_image.size[1]):
        # If the pixel is black in the QR code, replace it with the corresponding pixel from image_fill
        if qr_image.getpixel((x, y))[:3] == (0, 0, 0):  # Check if it's a black pixel
            final_qr.putpixel((x, y), image_fill.getpixel((x, y)))
        else:  # Otherwise, keep the pixel white
            final_qr.putpixel((x, y), (255, 255, 255, 255))

# Save the final QR code image
final_qr.save("Birthday_wishes_qr_with_image.png")

print("QR code with image fill generated and saved as 'wedding_invitation_qr_with_image.png'.")
