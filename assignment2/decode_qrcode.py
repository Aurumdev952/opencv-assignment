import cv2
from pyzbar.pyzbar import decode

def decode_qrcode(image_path):
    image = cv2.imread(image_path)
    qr_codes = decode(image)

    for qr in qr_codes:
        data = qr.data.decode("utf-8")
        print(f"Decoded QR Code: {data}")

        # Draw a rectangle around the QR code
        x, y, w, h = qr.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the image with the QR code highlighted
    cv2.imshow("QR Code", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
decode_qrcode("qrcode_assignment.png")
