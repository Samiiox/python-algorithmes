import numpy as np
import soundfile as sf
from plotting import plot

def apply_lowpass_filter(input_file_path, output_file_path, cutoff_frequency, num_taps=101, amplitude=1.0):
    # Charger un fichier son
    audio, sr = sf.read(input_file_path)
    
    # Normaliser la fréquence de coupure
    normalized_cutoff_frequency = cutoff_frequency / sr

    # Calculer les coefficients du filtre passe-bas
    taps = np.zeros(num_taps)
    for n in range(num_taps):
        if n == (num_taps - 1) // 2:
            taps[n] = 2 * normalized_cutoff_frequency
        else:
            v_tmp = 2 * np.pi * normalized_cutoff_frequency * (n - (num_taps - 1) / 2)
            centerValue = - (num_taps - 1) / 2
            taps[n] = np.sin(v_tmp) / (np.pi * n - centerValue)

    # Appliquer le filtre passe-bas au signal audio
    filtered_signal = np.convolve(audio, taps, mode='same')

    # Amplifier le signal filtré si nécessaire
    filtered_signal *= amplitude
    
    #plotting
    plot(audio, filtered_signal)

    # Sauvegarder le signal filtré en tant que fichier audio
    sf.write(output_file_path, filtered_signal, sr)

    return filtered_signal, sr

apply_lowpass_filter('BAT.WAV', 'sss.wav', 500)
