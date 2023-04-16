import numpy as np
import matplotlib.pyplot as plt



def convert_to_grayscale(image_path):
    # Charger l'image à partir du fichier
    img = plt.imread(image_path)

    # Extraire les dimensions de l'image
    height, width, channels = img.shape 

    gray_img = [[0 for j in range(width)] for i in range(height)]

    # Boucle sur chaque pixel de l'image
    for i in range(height):
        for j in range(width):
            # Extraire les valeurs de R, G et B du pixel
            r = img[i, j, 0]
            g = img[i, j, 1]
            b = img[i, j, 2]

            # Appliquer la formule de conversion en niveaux de gris
            gray_val = 0.2989 * r + 0.5870 * g + 0.1140 * b

            # Stocker la valeur de gris dans le tableau de sortie
            gray_img[i][j] = gray_val

    # Afficher l'image en niveaux de gris
    #plt.imshow(gray_img, cmap='gray')
    #plt.show()

    # Retourner le tableau de niveaux de gris
    return gray_img


def convert_to_binary(image_path, factor=128):
    # Convertir l'image en niveaux de gris en appelant convert_to_grayscale()
    gray_img = convert_to_grayscale(image_path)

    # Extraire les dimensions de l'image
    height, width = len(gray_img), len(gray_img[0])

    # Appliquer un seuil pour convertir en binaire
    binary_img = []
    for i in range(height):
        row = []
        for j in range(width):
            if gray_img[i][j] >= factor:
                row.append(1)
            else:
                row.append(0)
        binary_img.append(row)

    # Afficher l'image binaire
    plt.imshow(binary_img, cmap='gray')
    plt.show()

    return binary_img


convert_to_binary("image.jpeg")
