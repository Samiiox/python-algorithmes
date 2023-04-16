import numpy as np
import matplotlib.pyplot as plt





def convert_to_grayscale(image_path):
    # Charger l'image à partir du fichier
    img = plt.imread(image_path)

    # Extraire les dimensions de l'image
    height, width, channels = img.shape 

    # Créer un tableau pour les niveaux de gris, initialisé à zéro
    gray_img = np.zeros((height, width))


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

  

    # Retourner le tableau de niveaux de gris
    return gray_img



def detect_contours(image_path):
    # Charger l'image à partir du fichier
    img = plt.imread(image_path)

    # Convertir l'image en niveaux de gris
    gray = convert_to_grayscale(image_path)

    dx = np.zeros_like(gray)
    dy = np.zeros_like(gray)

    # Appliquer l'algorithme de Sobel pour détecter les contours
    for i in range(1, gray.shape[0]-1):
        for j in range(1, gray.shape[1]-1):
            dx[i,j] = (gray[i-1,j+1] + 2*gray[i,j+1] + gray[i+1,j+1]) \
                      - (gray[i-1,j-1] + 2*gray[i,j-1] + gray[i+1,j-1])
            dy[i,j] = (gray[i+1,j-1] + 2*gray[i+1,j] + gray[i+1,j+1]) \
                      - (gray[i-1,j-1] + 2*gray[i-1,j] + gray[i-1,j+1])

    magnitude = np.sqrt(dx**2 + dy**2)

    # Normaliser l'image de contours pour une meilleure visualisation
    threshold = (magnitude - np.min(magnitude)) / (np.max(magnitude) - np.min(magnitude))
    edges = np.zeros_like(threshold)
    for i in range(threshold.shape[0]):
        for j in range(threshold.shape[1]):
            if threshold[i,j] > 1:
                edges[i,j] = 1
            else:
                edges[i,j] = threshold[i,j]
    plt.imshow(edges,cmap='gray' )
    plt.show()
    # Retourner l'image de contours
    return edges

detect_contours("detect.png")






