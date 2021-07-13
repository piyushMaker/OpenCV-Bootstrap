######################## READ IMAGE ############################
import cv2
# LOAD AN IMAGE USING 'IMREAD'
img = cv2.imread("/Image/Path")
# DISPLAY
cv2.imshow("IMG_Display",img)
cv2.waitKey(0)