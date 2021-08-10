import numpy as np
import cv2
from PIL import Image, ImageDraw
import random
import matplotlib
import matplotlib.pyplot as plt
import copy

image = Image.open('Снимок (3).jpg')
image.show("Снимок (3).jpg")
arr = np.asarray(image, dtype='uint8')
mask=[[0,0,0],[0,0,0],[0,0,0]]

print(len(arr[2]))
width = image.size[0] 
height = image.size[1] 
print(arr)
ttt=cv2.imread('grom.jpg')
plt.hist(ttt.ravel(),256,[0,256])
plt.show()
draw = ImageDraw.Draw(image) 
print('=================')	
pix = image.load()
for i in range(width):
	for j in range(height):
		a = pix[i, j][0]
		b = pix[i, j][1]
		c = pix[i, j][2]
		draw.point((i, j), (255 - a, 255 - b, 255 - c))


image.save("ans3.jpg", "PNG")
image.show("ans3.jpg")

for i in range(width):
	for j in range(height):
			a = pix[i, j][0]
			b = pix[i, j][1]
			c = pix[i, j][2]
			S = (a + b + c) // 3
			draw.point((i, j), (S, S, S))
print('=================')
image.save("ans2.jpg", "PNG")
image.show("ans2.jpg")
for i in range(width):
	    for j in range(height):
		    a = pix[i, j][0]
		    b = pix[i, j][1]
		    c = pix[i, j][2]
		    S = a + b + c
		    if (S > (((255 + 99) // 2) * 3)):
		    	a, b, c = 255, 255, 255
		    else:
		    	a, b, c = 0, 0, 0
		    draw.point((i, j), (a, b, c))
image.save("ans.jpg", "PNG")
image.show("ans.jpg")

del draw
jojo=Image.open('ans2.jpg')
jiji=cv2.imread('ans2.jpg')


imgcv=cv2.imread('ans2.jpg',cv2.IMREAD_GRAYSCALE)
print(imgcv)
pix = image.load()
arr = np.asarray(imgcv, dtype='uint8')
print('=================')
arr2 = copy.copy(imgcv)
h, w = jiji.shape[:2]
i=1
j=1

print(imgcv)
k=0
while i<h-1:
        j=1
        while j<w-1:
            
                
                
                a=((imgcv[i-1][j+1])+2*(imgcv[i][j+1])+(imgcv[i+1][j+1]))-((imgcv[i-1][j-1])+2*(imgcv[i][j-1])+(imgcv[i+1][j-1]))
                bb=((imgcv[i-1][j-1])+2*(imgcv[i-1][j])+(imgcv[i-1][j+1]))-((imgcv[i+1][j-1])+2*(imgcv[i+1][j])+(imgcv[i+1][j+1]))
                arr2[i][j]=np.sqrt(a**2+bb**2)
                k+=1
                j+=1
        i+=1
cv2.imshow("Bruh", arr2)
