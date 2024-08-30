import cv2
pic = cv2.imread("bilateral.jpg")
shape = cv2.imread("diamond addition.jpeg")
tiger = cv2.imread("salt and pepper grains.jpeg")
star = cv2.imread("star addition.jpeg")
pok = cv2.imread("pika.png")
#add
add = cv2.addWeighted(star, 1, shape, 0.5, 0)
cv2.imshow("screen",add )
cv2.waitKey(0)
#subtraction of images
sub = cv2.subtract(star,shape)
cv2.imshow("screen2", sub)
cv2.waitKey(0)
#resize image
rs = cv2.resize(pic, (1480,1030))
cv2.imshow("screen3", rs)
cv2.waitKey(0)
#blurring # Gaussian Blur - used mostly in machine learning preprocessing steps# Median Blur - used in digital processing preserves edges but removes noise# Bilateral Blur - only sharp edges are preserved here
ga = cv2.GaussianBlur(pic, (11,11), 0, 0)
cv2.imshow("screen4", ga)
cv2.waitKey(0)
me = cv2.medianBlur(pic,7)
cv2.imshow("screen5", me)
cv2.waitKey(0)
bb = cv2.bilateralFilter(pic, 35, 250, 250)
cv2.imshow("screen6", bb)
cv2.waitKey(0)
#erosion
import numpy
matrix = numpy.ones((11, 11), numpy.uint8)
erosion = cv2.erode(pok, matrix)
cv2.imshow("screen7", erosion)
cv2.waitKey(0)