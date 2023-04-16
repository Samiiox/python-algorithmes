import numpy as np
import soundfile as sf
from plotting import plot

def remove_silence(input_file_path, output_file_path, silence_threshold=0.1, chunk_size=100):
    # Charger le fichier audio
    audio, sr = sf.read(input_file_path)

    # Calculer la valeur RMS moyenne
    rms = np.sqrt(np.mean(np.square(audio)))

    # Calculer le seuil de détection de silence
    threshold = rms * silence_threshold
    #Dans cet exemple, le seuil est déterminé en multipliant la valeur RMS moyenne du signal audio par le paramètre
    # "silence_threshold" qui est égal à 0.1. Cela signifie que toutes les parties du signal audio dont la puissance sonore est
    # inférieure à 10% de la puissance sonore moyenne du signal audio sont considérées comme silencieuses et sont supprimées.

    # Initialiser une liste pour stocker les tranches non silencieuses
    non_silent_chunks = []

    # Parcourir le signal audio par tranches de temps
    for i in range(0, len(audio), int(sr / 1000 * chunk_size)):#L'expression "int(sr / 1000 * chunk_size)" calcule le nombre d'échantillons dans chaque tranche de temps
        chunk = audio[i:i+int(sr / 1000 * chunk_size)]
        rms_chunk = np.sqrt(np.mean(np.square(chunk)))
        if rms_chunk > threshold:
            non_silent_chunks.append(chunk)


    #cette boucle permet de parcourir le signal audio en tranches de temps, de calculer la puissance sonore moyenne de chaque
    # tranche et de déterminer si elle est considérée comme silencieuse ou non en fonction du seuil de détection de silence.
    # Les tranches non silencieuses sont stockées dans une liste pour être fusionnées plus tard en un nouveau signal audio
    # sans les parties silencieuses.
    
    # Fusionner les tranches non silencieuses pour former un nouveau signal audio
    new_audio = np.concatenate(non_silent_chunks)
    # Une fois que toutes les tranches non silencieuses ont été identifiées et stockées dans la liste "non_silent_chunks",
    # la fonction "np.concatenate()" est appelée pour concaténer tous les tableaux de tranches non silencieuses en un seul tableau
    # "new_audio". Ce tableau "new_audio" représente le signal audio final sans silence

    # Sauvegarder le nouveau signal audio dans un nouveau fichier
    sf.write(output_file_path, new_audio, sr)
    
    plot(audio, new_audio)


remove_silence('detectSilence.wav','silenceRemoved.wav')