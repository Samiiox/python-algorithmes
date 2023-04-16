import numpy as np
import soundfile as sf
from plotting import plot

    
def apply_highpass_filter( input_file_path, ououtput_file_path, cutoff_frequency,
                          num_taps=101,amplitude=1.0):
            # Charger un fichier son
            audio, sr = sf.read(input_file_path)
            # Normaliser la fréquence de coupure
            normalized_cutoff_frequency = cutoff_frequency / sr
    
            # Calculer les coefficients du filtre passe-haut
            taps = np.zeros(num_taps)
            for n in range(num_taps):
                if n == (num_taps - 1) // 2:
                    taps[n] = 1 - 2 * normalized_cutoff_frequency
                else:
                    taps[n] = -(np.sin(2 * np.pi * normalized_cutoff_frequency *
                            (n - (num_taps - 1) / 2))) / (np.pi * (n - (num_taps - 1) / 2))
    
            # Appliquer le filtre passe-haut au signal audio
            filtered_signal = np.convolve(audio, taps, mode='same')
    
            # Amplifier le signal filtré si nécessaire
            filtered_signal *= amplitude
    
            # Sauvegarder le signal filtré en tant que fichier audio
            sf.write(ououtput_file_path, filtered_signal, sr)
            
            #plotting
            plot(audio, filtered_signal)
            
            return filtered_signal, sr

apply_highpass_filter('preamble10.wav','mm.wav',3000,num_taps=101,amplitude=1.0)
