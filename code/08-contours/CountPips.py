'''
 * Python program to use contours to count the pips on the dice faces.
 *
 * usage: python CountPips.py <filename> <threshold>
'''
import cv2, sys

# read command-line arguments
filename = sys.argv[1]
t = int(sys.argv[2])

# read original image
img = cv2.imread(filename)

# create binary image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
(t, binary) = cv2.threshold(blur, t, 255, cv2.THRESH_BINARY)

# find contours
(_, contours, hierarchy) = cv2.findContours(binary, cv2.RETR_CCOMP, 
    cv2.CHAIN_APPROX_SIMPLE)

# print table of contours and sizes
for (i, c) in enumerate(hierarchy[0]):
    print(i, c, sep='\t')

# draw contours over original image
cv2.drawContours(img, contours[17:24], -1, (0, 0, 255), 5)

# display original image with contours
cv2.namedWindow("output", cv2.WINDOW_NORMAL)
cv2.imshow("output", img)
cv2.waitKey(0)