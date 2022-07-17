import cv2
import random
import csv
import numpy as np
import webcolors as wbc

ragcolors = []
raghex = {}
ragcounts = []

# Read the Input.csv
with open('Input.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        print(row)
        ragcolors.append(row[0])
        raghex[row[0]] = row[1]
        ragcounts.append(int(row[2]))

print(ragcolors)
print(ragcounts)
ragtotal = sum(ragcounts)
ragrows = random.sample(ragcolors, k=ragtotal, counts=ragcounts)
print(ragrows)

width = 1024
height = 2048
img = np.zeros((height,width,3), np.uint8)
x = 0
stripeHeight = int(height/ragtotal)
print(stripeHeight)
for row in ragrows:
    rowcolor = wbc.name_to_rgb('Black')
    if (raghex[row] == ''):
        rowcolor = wbc.name_to_rgb(row)
    else:
        rowcolor = wbc.hex_to_rgb(raghex[row])
    cv2.line(img, (0,x), (height-1, x), (rowcolor.blue, rowcolor.green, rowcolor.red), stripeHeight)
    x = x + stripeHeight

cv2.imwrite('Output.png', img)
cv2.imshow('Output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
