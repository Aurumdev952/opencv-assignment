# pip install aspose-barcode-for-python-via-net

import aspose.barcode.barcoderecognition as barcode_recognition

image_path = 'assignment_image.png'

reader = barcode_recognition.BarCodeReader(image_path, barcode_recognition.DecodeType.PDF417)

for result in reader.read_bar_codes():
    print("Decoded Data:", result.code_text)
