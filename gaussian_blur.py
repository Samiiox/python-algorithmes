import numpy as np
import matplotlib.pyplot as plt

def gaussian_filter(img, sigma):
    size = int(2*np.ceil(3*sigma)+1) # Calculating the size of kernel
    kernel = np.zeros((size, size))
    center = size//2

    for i in range(size):
        for j in range(size):
            x = i - center
            y = j - center
            kernel[i,j] = (1 / (2 * np.pi * sigma**2)) * np.exp(-(x**2 + y**2) / (2 * sigma**2))

    kernel = kernel / np.sum(kernel)
    
    # Add padding to image
    padded_img = np.pad(img, ((center, center), (center, center), (0, 0)), mode='edge')

    result = np.zeros_like(img)

    width, height, n_channels = img.shape

    for z in range(n_channels):
        for i in range(center, width + center):
            for j in range(center, height + center):
                result[i-center,j-center,z] = np.sum(padded_img[i-center:i+center+1, j-center:j+center+1, z] * kernel)

    return result

def apply_gaussian_blur(image_path, sigma):
    # Load image
    image = plt.imread(image_path)
    # Apply Gaussian blur
    blurred_image = gaussian_filter(image, sigma=sigma)
    plt.imshow(blurred_image)
    plt.show()   
    
    return image, blurred_image

apply_gaussian_blur("aa.jpg", 8)
