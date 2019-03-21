#Author: Austin Johnson
import cv2
import numpy as np

# Print number of candies
def printCount(img, redCount, greenCount, blueCount, yellowCount, orangeCount, brownCount):
    cv2.putText(img, "Red Count: " + str(redCount), (5, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(img, "Green Count: " + str(greenCount), (5, 475), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(img, "Blue Count: " + str(blueCount), (5, 500), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(img, "Yellow Count: " + str(yellowCount), (5, 525), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(img, "Orange Count: " + str(orangeCount), (5, 550), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(img, "Brown Count: " + str(brownCount), (5, 575), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1, cv2.LINE_AA)

# Get center RGB
def getCenter(pic, x, y):
    red = int(pic[y][x][2])
    green = int(pic[y][x][1])
    blue = int(pic[y][x][0])
    return red, green, blue

# Assign color using a threshold of rgb values
def setColor(red, green, blue):
    color = 0
    if((red <= 255 and red >= 160) and (green <= 150 and green >= 55) and (blue <= 190 and blue >= 70)):
        #Red
        color = 1
    if((red <= 60 and red >= 0) and (green <= 255 and green >= 165) and (blue <= 210 and blue >= 70)):
        #Green
        color = 2
    if((red <= 35 and red >= 0) and (green <= 235 and green >= 120) and (blue <= 255 and blue >= 220)):
        #Blue
        color = 3
    if((red <= 255 and red >= 200) and (green <= 255 and green >= 200) and (blue <= 170 and blue >= 0)):
        #Yellow
        color = 4
    if((red <= 160 and red >= 0) and (green <= 160 and green >= 0) and (blue <= 180 and blue >= 0)):
        #Brown
        color = 5
    if((red <= 255 and red >= 220) and (green <= 200 and green >= 90) and (blue <= 55 and blue >= 0)):
        #Orange
        color = 6
    return color

def main():
    # Read pictures, blur, find edges, and circles.
    picture1 = cv2.imread("imagesWOvideo/one.jpg", cv2.IMREAD_COLOR)
    picture2 = cv2.imread("imagesWOvideo/two.jpg", cv2.IMREAD_COLOR)
    picture3 = cv2.imread("imagesWOvideo/three.jpg", cv2.IMREAD_COLOR)
    picture4 = cv2.imread("imagesWOvideo/four.jpg", cv2.IMREAD_COLOR)
    blur1 = cv2.GaussianBlur(picture1, (5, 5), 1)
    blur2 = cv2.GaussianBlur(picture2, (5, 5), 1)
    blur3 = cv2.GaussianBlur(picture3, (5, 5), 1)
    blur4 = cv2.GaussianBlur(picture4, (5, 5), 1)
    edge1 = cv2.Canny(blur1, 200, 150)
    edge2 = cv2.Canny(blur2, 200, 150)
    edge3 = cv2.Canny(blur3, 200, 150)
    edge4 = cv2.Canny(blur4, 200, 150)
    circle1 = cv2.HoughCircles(edge1, cv2.HOUGH_GRADIENT, 1, 35, param1=1, param2=35, minRadius=8, maxRadius=0)
    circle2 = cv2.HoughCircles(edge2, cv2.HOUGH_GRADIENT, 1, 35, param1=1, param2=33, minRadius=8, maxRadius=0)
    circle3 = cv2.HoughCircles(edge3, cv2.HOUGH_GRADIENT, 1, 35, param1=1, param2=36, minRadius=8, maxRadius=0)
    circle4 = cv2.HoughCircles(edge4, cv2.HOUGH_GRADIENT, 1, 35, param1=1, param2=50, minRadius=8, maxRadius=0)
    circles1 = np.uint16(np.around(circle1))
    circles2 = np.uint16(np.around(circle2))
    circles3 = np.uint16(np.around(circle3))
    circles4 = np.uint16(np.around(circle4))

    #Saving center locations of the circles
    centerOfCircle1 = []
    for i in circles1[0, :]:
        centerOfCircle1.append((i[0],i[1]))
    centerOfCircle2 = []
    for i in circles2[0, :]:
        centerOfCircle2.append((i[0],i[1]))
    centerOfCircle3 = []
    for i in circles3[0, :]:
        centerOfCircle3.append((i[0], i[1]))
    centerOfCircle4 = []
    for i in circles4[0, :]:
        centerOfCircle4.append((i[0], i[1]))

    #Counting for picture 1
    redCount, greenCount, blueCount, yellowCount, orangeCount, brownCount, color = (0,0,0,0,0,0,0)
    color = ""
    for i in range(len(centerOfCircle1)):
        r, g, b = getCenter(picture1, centerOfCircle1[i][0], centerOfCircle1[i][1])
        color = setColor(r,g,b)
        if(color == 1):
            redCount += 1
        if(color == 2):
            greenCount += 1
        if(color == 3):
            blueCount += 1
        if(color == 4):
            yellowCount += 1
        if(color == 5):
            orangeCount += 1
        if(color == 6):
            brownCount += 1
        cv2.circle(picture1,(centerOfCircle1[i][0], centerOfCircle1[i][1]),4,(255,255,255),-1)
    printCount(picture1, redCount, greenCount, blueCount, yellowCount, orangeCount, brownCount)

    #Counting for picture 2
    redCount, greenCount, blueCount, yellowCount, orangeCount, brownCount, color = (0,0,0,0,0,0,0)
    for i in range(len(centerOfCircle2)):
        r, g, b = getCenter(picture2, centerOfCircle2[i][0], centerOfCircle2[i][1])
        color = setColor(r,g,b)
        if(color == 1):
            redCount += 1
        if (color == 2):
            greenCount += 1
        if (color == 3):
            blueCount += 1
        if (color == 4):
            yellowCount += 1
        if (color == 5):
            orangeCount += 1
        if (color == 6):
            brownCount += 1
        cv2.circle(picture2,(centerOfCircle2[i][0], centerOfCircle2[i][1]),4,(255,255,255),-1)
    printCount(picture2, redCount, greenCount, blueCount, yellowCount, orangeCount, brownCount)

    #Counting for picture 3
    redCount, greenCount, blueCount, yellowCount, orangeCount, brownCount, color = (0,0,0,0,0,0,0)
    for i in range(len(centerOfCircle3)):
        r, g, b = getCenter(picture3, centerOfCircle3[i][0], centerOfCircle3[i][1])
        color = setColor(r,g,b)
        if(color == 1):
            redCount += 1
        if (color == 2):
            greenCount += 1
        if (color == 3):
            blueCount += 1
        if (color == 4):
            yellowCount += 1
        if (color == 5):
            orangeCount += 1
        if (color == 6):
            brownCount += 1
        cv2.circle(picture3,(centerOfCircle3[i][0], centerOfCircle3[i][1]),4,(255,255,255),-1)
    printCount(picture3, redCount, greenCount, blueCount, yellowCount, orangeCount, brownCount)

    #Counting for picture 4
    redCount, greenCount, blueCount, yellowCount, orangeCount, brownCount, color = (0,0,0,0,0,0,0)
    for i in range(len(centerOfCircle4)):
        r, g, b = getCenter(picture4, centerOfCircle4[i][0], centerOfCircle4[i][1])
        color = setColor(r,g,b)
        if(color == 1):
            redCount += 1
        if (color == 2):
            greenCount += 1
        if (color == 3):
            blueCount += 1
        if (color == 4):
            yellowCount += 1
        if (color == 5):
            orangeCount += 1
        if (color == 6):
            brownCount += 1
        cv2.circle(picture4,(centerOfCircle4[i][0], centerOfCircle4[i][1]),4,(255,255,255),-1)
    printCount(picture4, redCount, greenCount, blueCount, yellowCount, orangeCount, brownCount)

    cv2.namedWindow("Candy1", cv2.WINDOW_KEEPRATIO)
    cv2.moveWindow("Candy1", 0, 0)
    cv2.imshow("Candy1", picture1)
    cv2.namedWindow("Candy2", cv2.WINDOW_KEEPRATIO)
    cv2.moveWindow("Candy2", 500, 0)
    cv2.imshow("Candy2", picture2)
    cv2.namedWindow("Candy3", cv2.WINDOW_KEEPRATIO)
    cv2.moveWindow("Candy3", 0, 400)
    cv2.imshow("Candy3", picture3)
    cv2.namedWindow("Candy4", cv2.WINDOW_KEEPRATIO)
    cv2.moveWindow("Candy4", 500, 400)
    cv2.imshow("Candy4", picture4)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()
