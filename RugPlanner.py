import cv2
import random
import csv
import numpy as np

ragcolors = []
ragcounts = []

# Read the Input.csv
with open('Input.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        print(row)
        ragcolors.append(row[0])
        ragcounts.append(int(row[1]))

print(ragcolors)
print(ragcounts)
ragtotal = sum(ragcounts)
ragrows = random.sample(ragcolors, k=ragtotal, counts=ragcounts)
print(ragrows)

#img = cv2.imread('Output.png')
img = np.zeros((512,512,3), np.uint8)
cv2.line(img, (0,0), (511, 0), (255,0,0), 5)
cv2.imshow('Output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
