import cv2


image_path = 'car-license-plate-jaw-640x400.jpg'
# خواندن تصویر با استفاده از OpenCV
image = cv2.imread(image_path)

# تبدیل تصویر به سیاه و سفید (گریس‌اسکیل)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# اعمال فیلترهای پردازش تصویر برای بهبود خوانایی
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
edged_image = cv2.Canny(blurred_image, 50, 150)

# یافتن کانتورهای تصویر
contours, _ = cv2.findContours(edged_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# انتخاب بزرگ‌ترین کانتور (احتمالا کانتور پلاک)
largest_contour = max(contours, key=cv2.contourArea)

# استخراج مستطیل محدودکننده پلاک
x, y, w, h = cv2.boundingRect(largest_contour)

## برش تصویر پلاک
license_plate = gray_image[y:y + h, x:x + w]

cv2.imshow('Image', license_plate)
cv2.waitKey(0)
cv2.destroyAllWindows()
