import numpy as np
import matplotlib.pyplot as plt


def convert_to_grayscale(image_path):
    img = plt.imread(image_path)

    height, width, channels = img.shape 

    gray_img = [[0 for j in range(width)] for i in range(height)]

    for i in range(height):
        for j in range(width):
            r = img[i, j, 0]
            g = img[i, j, 1]
            b = img[i, j, 2]

            gray_val = 0.2989 * r + 0.5870 * g + 0.1140 * b

            gray_img[i][j] = gray_val
            
    plt.imshow(gray_img,cmap='gray' )
    plt.show()        

    return gray_img


gray_img = convert_to_grayscale("img/image.jpeg")







