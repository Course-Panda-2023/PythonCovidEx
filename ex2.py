import numpy as np
from PIL import Image
import cv2
# import png



data = np.load('ex2/mysterious_file.npz')
image = data['arr_0']
img = Image.fromarray(image.astype(np.uint8))
img.save('ex2/myst.png')


img1 = cv2.imread('ex2/noised_img.png')
img2 = cv2.imread('ex2/myst.png')

sub_img = cv2.subtract(img1, img2)


# cv2.imshow("Image 1", img1)
# cv2.imshow("Image 2", img2)
cv2.imshow("Image Subtraction", sub_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
