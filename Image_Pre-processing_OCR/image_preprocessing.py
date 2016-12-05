import cv2
import numpy as np
from matplotlib import pyplot as plt

# For handwritten notes the sequence of preprocessing should be as follows:- 
# resizing
# Clustering if loading in color else load in grayscale 
# Image filtering to reduce noise in grayscale image, the choise of filters depends on the type of noise 
# Histogram Equalisation 
# Thresholding 
# Binarization
# Smoothing ----- this is only necessary for handwritten mode, and not for the screep capture mode

# ******************** Resize ******************************
def resize(img):
  # resizing image for standardization
  x,y = img.shape[:2]
  print str(x)+" "+str(y)
  x=float(1200/float(x))
  y=float(1200/float(y))
  print x,; print y
  res = cv2.resize(img,None,fx=float(x), fy=float(y), interpolation = cv2.INTER_LINEAR)
  return res
# ******************** Orientation Correction *****************

#**************************************************************
# ******************** Image smoothing ************************
def convolutional_blur(img):
  # simple 2D convolutional image filter / averaging
  kernel = np.ones((3,3),np.float32)/25 #creates a 3X3 kernel of ones 
  dst = cv2.filter2D(img,-1,kernel)
  return dst
def gaussian_blur(img):
  # gaussian blurring 
  gaussian = cv2.GaussianBlur(img,(3,3),0)
  return gaussian
def median_blur(img):
  # median blurring- highly effective against salt and pepper noise
  median= cv2.medianBlur(img,5)
  return median
def bilateralFilter(img):
  # Bilateral Filtering- highly effective in noise removal while keeping edges sharp
  bilateral= cv2.bilateralFilter(img,9,75,75) 
  return bilateral
def smooth_image(img):
  # blur the image to reduce noise 
  dst= median_blur(img)
  dst= gaussian_blur(dst)
  dst= bilateralFilter(dst)
  return dst
# *********************************************************

# ************************** Binarization *****************
def adaptive_thresholding(img):
  # adaptive mean binary threshold
  th4 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
  # adaptive gaussian thresholding
  th5 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
  return th5
def otsu_binarisation(img):
  # global thresholding
  ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
  # Otsu's thresholding
  ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
  # Otsu's thresholding after Gaussian filtering
  blur = cv2.GaussianBlur(img,(3,3),0)
  ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
  return th3
# *********************************************************

# ****************** Histogram Equilization ***************
def hist_equalise(img):
  eq=cv2.equalizeHist(img)
  return eq
# *********************************************************

# ****************** Cluster image ************************

# *********************************************************

if __name__=='__main__':
  img = cv2.imread('../testing/images_for_test/one.jpg',0)
  cv2.imwrite("../testing/output_images/loaded_image.jpg",img)
  img=resize(img)
  cv2.imwrite("../testing/output_images/resized_image.jpg",img)
  th= smooth_image(img) 
  th= hist_equalise(th)
  cv2.imwrite("../testing/output_images/equalized.jpg",th)
  th= adaptive_thresholding(th)
  th= otsu_binarisation(th)
  th= smooth_image(th) 
  cv2.imwrite("../testing/output_images/smoothed_adaptive_Gaussian_threshold_otsu_binarization.jpg",th)

  