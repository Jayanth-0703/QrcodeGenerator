import qrcode
from qrcode.constants import ERROR_CORRECT_L

def generate_qr(link, filename="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(filename, format="PNG")  # Explicitly saving as PNG format
    print(f"QR Code saved as {filename}")

if __name__ == "__main__":
    url = input("Enter the link to generate QR Code: ")
    generate_qr(url)
