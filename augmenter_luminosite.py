import numpy as np
import matplotlib.pyplot as plt


def augmenter_luminosite(image_path, factor):
    # Charger l'image à partir du fichier
    img = plt.imread(image_path)

    # Extraire les dimensions de l'image
    height, width, channels = img.shape

    # Initialiser la liste pour stocker l'image modifiée
    new_img = [[0 for j in range(width)] for i in range(height)]

    # Parcourir chaque pixel de l'image
    for x in range(width):
        for y in range(height):
            # Extraire les valeurs de R, G et B du pixel
            r, g, b = img[y, x, :]

            # Augmenter la valeur de chaque canal RGB
            new_r = min(int(r * factor), 255)
            new_g = min(int(g * factor), 255)
            new_b = min(int(b * factor), 255)

            # Définir la nouvelle couleur du pixel dans l'image modifiée
            new_img[y][x] = [new_r, new_g, new_b]
   
    # Afficher l'image avec luminosité augmentée
    plt.imshow(new_img)
    plt.show()

# Exemple d'utilisation
augmenter_luminosite("image.jpeg", 2) # Augmente la luminosité de 50%





