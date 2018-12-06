import OrderStat as OS
import random as random
import numpy as np
import time
import matplotlib as mpl

import numpy as np
import matplotlib.pyplot as plt

#Image libraries
from urllib.request import urlopen
from PIL import Image, ImageMath
from scipy import ndimage
import matplotlib.image as mpimg

def setup():
  N = [5000,8000,10000]
  n = [100,300,500,1000,2000,4000]
  arr = []
  running_times = []
  run = 0
  ##########################################
  for a in N:
    times = [] #Holds our running times for the current N
    ########################################
    for b in n:
      for a in range(0, a+1):
        arr.append(random.randrange(1, b+1))
      #####################################
      run += 1
      i = random.randrange(b)
      ###### Runs our algorithm ######
      start = time.clock()
      value = OS.KthSmallest(arr.copy(), 0 , a , i)
      end = time.clock() - start
      ###### Outputs the results and times ######
      times.append(end)
      print("=== Run %d | N = %d | n = %d | i = %d ===" % (run,a,b, i))
      print("%dth Smallest Element: %d" % (i, value))
      print("=== Time Taken: %s === \n" % end)
      ###### Appends the list of runtimes to our return array #########
    running_times.append(times) 
  return running_times

#Returns a window as a list
def getWindow(image, step = 3, rowIndex = 0, colIndex = 0):
  li = []
  for i in range(0,step):
    copy = image[rowIndex:rowIndex+step,colIndex:colIndex+step][i]
    for j in copy:
      li.append(j)
  return li

def show_img(img):
    plt.figure()
    plt.imshow(img, cmap='gray', aspect='auto')
    plt.show()


def gauss_noise(image):
  row,col= image.shape
  mean = 0
  var = 0.1
  sigma = var**0.5
  gauss = np.random.normal(mean,sigma,(row,col))
  gauss = gauss.reshape(row,col)
  noisy = image + gauss
  return noisy

def saltpepper(image):
    row,col = image.shape
    s_vs_p = 0.5
    amount =  0.05  #0.004
    out = np.copy(image)
    # Applys random white pixels to the image
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    out[coords] = 1

    # Applies random black dots to the image
    num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper))
            for i in image.shape]
    out[coords] = 0
    return out


def medianFilter(image, step_size = 3):
  new_img = np.zeros(image.shape)
  R, C = new_img.shape
  
  mid = int(step_size/2)
  winmed = int((step_size**2)/2 + 1)
  m = (step_size**2)/2 + 1
  for cols in range(C - (step_size -1)):
      for rows in range(R - (step_size -1)):
        win = getWindow(image, step=step_size, rowIndex=rows, colIndex=cols)
        median = OS.KthSmallest(win.copy(), 0, (step_size**2)-1, m)
        new_img[rows+mid][cols+mid] = median
  return new_img

'''
run_times = []
run_times = setup()
r1 = run_times[0]
r2 = run_times[1]
r3 = run_times[2]
b = [100,300,500,1000,2000,4000]
plt.plot(b, r3)
plt.savefig('graph.png')
'''
pixels = mpimg.imread("B5EhD.png", 0)
#noise = saltpepper(pixels)
show_img(pixels)
print(pixels.shape)


pixels = np.pad(pixels,pad_width=(1,1), mode='constant', constant_values=0)

mid = int(3/2)
winmed = int((3*3)/2 + 1)
print(winmed)
for cols in range(pixels.shape[1] - 2):
  for rows in range(pixels.shape[0] - 2):
    win = getWindow(pixels, step = 3, rowIndex = rows, colIndex = cols)
    l = len(win)
    medi = OS.KthSmallest(win.copy(), 0, l - 1, winmed)
    pixels[rows+mid,cols+mid] = medi

plt.imshow(pixels, cmap='gray', aspect='auto')
plt.title("Median Filter")
plt.show()

