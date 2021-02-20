import cv2 as cv
import numpy as np
from skimage.util import random_noise


def Average_Image(Imagelist, Count):
    Avg_Img = np.array(Imagelist[0], 'f')
    if Count == 5:
        print(len(Avg_Img), len(Avg_Img[0]))

    for i in range(Count-1):
        Avg_Img = Avg_Img + np.array(Imagelist[i+1])

    Avg_Img = Avg_Img / Count

    return np.array(Avg_Img, 'uint8')


def main():
    img = cv.imread('Lena_Image.jpeg', 0)
    cv.imshow('Original Image', img)

    Gaussian_noise = []
    SaltAndPepper_noise = []
    Speckle_noise = []

    for i in range(30):
        Gaussian_noise.append(random_noise(img, mode = 'gaussian'))
        Gaussian_noise[i] = np.array(255*Gaussian_noise[i], dtype = 'uint8')
        SaltAndPepper_noise.append(random_noise(img, mode = 's&p'))
        SaltAndPepper_noise[i] = np.array(255*SaltAndPepper_noise[i], dtype = 'uint8')
        Speckle_noise.append(random_noise(img, mode = 'speckle'))
        Speckle_noise[i] = np.array(255*Speckle_noise[i], dtype = 'uint8')

    Avg_Gaussian = []
    Avg_SaltAndPepper = []
    Avg_Speckle = []
    Set_Count = [5, 10, 15, 20, 25, 30]
    
    for i in Set_Count:
        Avg_Gaussian.append(Average_Image(Gaussian_noise, i))
        Avg_SaltAndPepper.append(Average_Image(SaltAndPepper_noise, i))
        Avg_Speckle.append(Average_Image(Speckle_noise, i))
    
    for i in range(len(Set_Count)):
        cv.imshow('Average of ' + str(Set_Count[i]) + ' Gaussian Noisy Images', Avg_Gaussian[i])
        cv.imshow('Average of ' + str(Set_Count[i]) + ' Salt and Pepper Noisy Images', Avg_SaltAndPepper[i])
        cv.imshow('Average of ' + str(Set_Count[i]) + ' Speckle Noisy Images', Avg_Speckle[i])

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()