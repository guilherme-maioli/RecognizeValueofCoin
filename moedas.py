import cv2 as cv
import numpy as np

#finds the contours of the objects
img2 = cv.imread('teste3.jpg')
output = img2.copy()

img = cv.imread('teste3.jpg')
img = cv.blur(img,(10, 10))

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# circles = cv.HoughCircles(gray, cv.cv.CV_HOUGH_GRADIENT, 1.2, 100) # python 2.7

circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1.2, 100) # python 3.7


count = 0
valor = 0

if circles is not None:

    circles = np.round(circles[0, :]).astype("int")

    for (x, y, r) in circles:
        count = count + 1
        cv.circle(output, (x, y), r, (0, 255, 0), 4)
        cv.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

        if r < 50:
        	valor = valor + 0.01

        elif (r > 50) & (r < 60):
        	valor = valor  + 0.10

        elif (r > 60) & (r < 70):
        	valor = valor + 0.50

        else:
        	valor = valor + 1

    numMoedas = "A imagem contem: " + str(count) + " moedas."
    valorMoedas = "A imagem contem: R$ " 
    
    font = cv.FONT_HERSHEY_TRIPLEX 
    
    cv.putText(output, numMoedas, (10,400), font, 1, (0,0,0), 2)
    cv.putText(output, valorMoedas+"%.2f" % round(valor,2), (10,450), font, 1, (0,0,0), 2)

    cv.imshow("Output", np.hstack([img2, output]))

    cv.waitKey(0)
    cv.destroyWindows()
    
cv.destroyAllWindows()