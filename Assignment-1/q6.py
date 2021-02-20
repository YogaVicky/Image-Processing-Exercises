import cv2 as cv
import numpy as np
from numpy import asarray
from PIL import Image
from matplotlib import pyplot as plt
import math

#Image->Array
def convitoa(im_path):
    img=Image.open(im_path)
    im_array=asarray(img)
    return im_array

#Array->Image
def convatoi(im_array):
    data=Image.fromarray(im_array)
    data.save('gfg_dummy_pic.png') 

def imgconv(cdf,im_array):
    dim=im_array.shape
    x=dim[0]
    y=dim[1]
    z=dim[2]
    new_im=np.arange(0,171054, 1, np.uint8).reshape(x,y,z)
    for i in range(x):
        for j in range(y):
            for k in range(z):
                new_im[i][j][k]=cdf[im_array[i][j][k]]
    return new_im


# create histogram and convert into probability distribution and create a lookup table 
def create_hist(im_path):
    sum=0
    img1=cv.imread(im_path,0)
    count=cv.calcHist([img1],[0],None,[256],[0,256])
    for i in range(len(count)):
        sum+=count[i]
    prob_dist=count/sum


    cdf=prob_dist

    sum=0
    for i in range(1,len(prob_dist)):
        cdf[i]=(cdf[i-1]+cdf[i])
        cdf[i-1]=int(math.floor(cdf[i-1]*255))
    cdf[-1]*=255
    cdf[-1]=int(cdf[-1])
    return count,cdf

    



def main():
    im_path="pout-dark.jpg"
    im_array=convitoa(im_path)
    count,cdf=create_hist(im_path)
    im_array=imgconv(cdf,im_array)
    convatoi(im_array)
    






if __name__=="__main__":
    main()
