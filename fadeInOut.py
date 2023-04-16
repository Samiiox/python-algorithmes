import numpy as np
import soundfile as sf


def apply_fade(input_file_path, fade_duration):
    # Charger un fichier son
    audio, sr = sf.read(input_file_path)

    # Calculer le nombre d'échantillons pour le fade
    fade_samples = int(fade_duration * sr)

    # Créer les tableaux pour le fade-in et le fade-out
    fade_in = np.linspace(0, 1, fade_samples, endpoint=False)
    fade_out = np.linspace(1, 0, fade_samples, endpoint=False)

    # Appliquer le fade-in
    audio[:fade_samples] *= fade_in

    # Appliquer le fade-out
    audio[-fade_samples:] *= fade_out

apply_fade('uuu.wav',5)



