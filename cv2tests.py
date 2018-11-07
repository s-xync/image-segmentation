import cv2

my_img = cv2.imread('input.jpg')
# cv2.imshow("MyImage", my_img),
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imwrite('output.jpg',my_img)

print(my_img[200][400])