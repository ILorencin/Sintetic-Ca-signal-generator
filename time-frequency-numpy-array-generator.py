import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import random
import os
import csv
import generate_signals  # module for signal generating

# Create a directory to save the signals
directory = 'signals'
directory2 = 'time-frequency'
os.makedirs(directory, exist_ok=True)
os.makedirs(directory2, exist_ok=True)

num_signals = 1000
num_samples = 1000
time_limit = 30

# Generate two types of calcium imaging signals (one peak and two peaks)
signals1, time = generate_signals.generate_ca_signals(num_signals, num_samples, time_limit, signal_type=0)
signals2, time = generate_signals.generate_ca_signals(num_signals, num_samples, time_limit, signal_type=1)

# Join and shuffle the signals
signals = signals1 + signals2
random.shuffle(signals)

# Save generated signals to CSV
with open('generated_signals.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(signals)

# Initialize an empty array to store spectrograms
spectrograms = []

# Plotting and saving loop
for i, si in enumerate(signals):
    # Compute the time-frequency representation using spectrogram
    frequencies, times, spectrogram = signal.spectrogram(si, fs=1.0 / (time[1] - time[0]),
                                                        nperseg=128, noverlap=64, mode='magnitude')
    # Append spectrogram to the array
    spectrograms.append(spectrogram)

    # Plot calcium imaging-like signal
    plt.figure(figsize=(8, 4))
    plt.ylim(-1, 11)
    plt.plot(time, si)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Generated Calcium Imaging Signal')
    plt.savefig(os.path.join(directory, f'signal_{i+1}_time_domain.png'), format='png')
    #plt.show()
    plt.close()

    # Plot the time-frequency representation
    plt.figure(figsize=(8, 4))
    plt.pcolormesh(times, frequencies, 0.01 * np.log10(spectrogram), shading='auto', cmap='jet')
    plt.colorbar(label='Magnitude')
    plt.ylim(0, 17)
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.title('Time-Frequency Representation')
    plt.tight_layout()
    plt.savefig(os.path.join(directory2, f'signal_{i+1}_time_frequency.png'), format='png')
    #plt.show()
     plt.close()

# Convert the spectrograms list to a NumPy array
spectrograms = np.array(spectrograms)

# Save the spectrograms as a NumPy array
np.save('spectrograms.npy', spectrograms)
