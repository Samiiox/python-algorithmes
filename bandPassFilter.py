import numpy as np
import soundfile as sf
from plotting import plot

def apply_bandpass_filter(input_file, output_file, low_cutoff_frequency, high_cutoff_frequency,
                          num_taps=101, amplitude=1.0):
    # Charger un fichier son
    audio, sr = sf.read(input_file)

    # Normaliser les fréquences de coupure
    normalized_low_cutoff_frequency = low_cutoff_frequency / sr
    normalized_high_cutoff_frequency = high_cutoff_frequency / sr

    # Calculer les coefficients du filtre passe-bande
    taps = np.zeros(num_taps)
    for n in range(num_taps):
        if n == (num_taps - 1) // 2:
            taps[n] = 2 * (normalized_high_cutoff_frequency - normalized_low_cutoff_frequency)
        else:
            high_freq_sinus = np.sin(2 * np.pi * normalized_high_cutoff_frequency *
                                     (n - (num_taps - 1) / 2))
            low_freq_sinus = np.sin(2 * np.pi * normalized_low_cutoff_frequency *
                                    (n - (num_taps - 1) / 2))
            taps[n] = (high_freq_sinus - low_freq_sinus) / (np.pi * (n - (num_taps - 1) / 2))

    # Appliquer le filtre passe-bande au signal audio
    filtered_signal = np.convolve(audio, taps, mode='same')

    # Amplifier le signal filtré si nécessaire
    filtered_signal *= amplitude
    
    #plotting
    plot(audio, filtered_signal)

    # Sauvegarder le signal filtré en tant que fichier audio
    sf.write(output_file, filtered_signal, sr)
    
    return filtered_signal,sr

apply_bandpass_filter('preamble10.wav', 'SET.wav', 500, 5000)

