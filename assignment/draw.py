import cv2

image_path = "./assignment-001-given.jpg"
image = cv2.imread(image_path)


window_name = "Select License Plate"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.imshow(window_name, image)


print("Select the license plate area and press ENTER or SPACE to confirm.")
selected_roi = cv2.selectROI(window_name, image, showCrosshair=True)
cv2.destroyAllWindows()


x, y, w, h = map(int, selected_roi)


cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 8)

license_plate_text = "RAH972U"

font_scale = 3
font_thickness = 6
text_size = cv2.getTextSize(
    license_plate_text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_thickness
)[0]

text_offset_x = 60
text_x = x + w - text_size[0] - 10 + text_offset_x
text_y = y - 20

overlay = image.copy()
background_x1 = text_x - 10
background_y1 = text_y - text_size[1] - 10
background_x2 = text_x + text_size[0] + 10
background_y2 = text_y + 10
cv2.rectangle(
    overlay,
    (background_x1, background_y1),
    (background_x2, background_y2),
    (0, 0, 0),
    -1,
)

alpha = 0.4
cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)

cv2.putText(
    image,
    license_plate_text,
    (text_x, text_y),
    cv2.FONT_HERSHEY_SIMPLEX,
    font_scale,
    (0, 255, 0),
    font_thickness,
)

output_path = "selected_license_plate_with_text.jpg"
cv2.imwrite(output_path, image)

print(f"{output_path}.")
