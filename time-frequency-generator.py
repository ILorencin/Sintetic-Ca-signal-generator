import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import os

def generate_signals(num_signals,num_samples, duration,signal_type=0):
    # Parameters

    if signal_type==0:
        signals = []
    
        for _ in range(num_signals):
            # Generate time axis
            
    
            # Generate random parameters for each signal
            spike_locations = [500,6000]
            noise_level = noise_level = 0.0001  # Maximum noise level
            spike_amplitude = np.random.uniform(5.0, 10.0)
            decay_time = np.random.uniform(0.1, 0.2)
            
            
    
            # Generate noise
            noise = np.random.uniform(-noise_level, noise_level, num_samples)
    
            # Generate spike waveform
            spike_waveform = np.zeros(num_samples)
            rise_time = 0.01  # Time taken for spike to rise
    
            for location in spike_locations:
                spike_waveform[location+1:int(location+rise_time*num_samples)] += np.linspace(0, spike_amplitude, int(rise_time*num_samples)-1)
                # Exponential decay
                decay_samples = int((decay_time - rise_time) * num_samples)
                decay_range = np.linspace(spike_amplitude, 0, decay_samples)
                decay_factor = np.exp(-5 * np.linspace(0, 1, decay_samples))  # Exponential decay factor
                spike_waveform[int(location+rise_time*num_samples):int(location+decay_time*num_samples)] += decay_range * decay_factor
    
            # Combine noise and spike waveform
            signal = noise + spike_waveform
    
            # Add the generated signal to the list
            signals.append(signal)
            
            
    if signal_type==1:
        signals = []
    
        for _ in range(num_signals):
            # Generate time axis
            
    
            # Generate random parameters for each signal
            spike_locations = [6000]
            noise_level = noise_level = 0.0001  # Maximum noise level
            spike_amplitude = np.random.uniform(5.0, 10.0)
            decay_time = np.random.uniform(0.1, 0.2)
            
    
            # Generate noise
            noise = np.random.uniform(-noise_level, noise_level, num_samples)
    
            # Generate spike waveform
            spike_waveform = np.zeros(num_samples)
            rise_time = 0.01  # Time taken for spike to rise
    
            for location in spike_locations:
                spike_waveform[location+1:int(location+rise_time*num_samples)] += np.linspace(0, spike_amplitude, int(rise_time*num_samples)-1)
                # Exponential decay
                decay_samples = int((decay_time - rise_time) * num_samples)
                decay_range = np.linspace(spike_amplitude, 0, decay_samples)
                decay_factor = np.exp(-5 * np.linspace(0, 1, decay_samples))  # Exponential decay factor
                spike_waveform[int(location+rise_time*num_samples):int(location+decay_time*num_samples)] += decay_range * decay_factor
    
            # Combine noise and spike waveform
            signal = noise + spike_waveform
    
            # Add the generated signal to the list
            signals.append(signal)

    return signals,num_samples

# Generate multiple signals
num_signals = 50
duration = 30.0
signals, num_samples = generate_signals(num_signals,10000, duration,signal_type=1)

# Create a directory to save the signals
directory = 'signals'
directory2='time-frequency'
os.makedirs(directory, exist_ok=True)

# Plot the signals and generate time-frequency representation
for i, si in enumerate(signals):
    # Plot and save the signal in the time domain
    plt.figure(figsize=(8, 4))
    plt.plot(np.linspace(0,num_samples,num_samples),si)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title(f'Signal {i+1}')
    plt.savefig(os.path.join(directory, f'signal_{i+1}_time_domain.png'), format='png')
    plt.close()

    # Compute the time-frequency representation using spectrogram
    frequencies, times, spectrogram = signal.spectrogram(si, fs=1.0 / (si[1] - si[0]), nperseg=512, noverlap=256)

    # Plot the time-frequency representation
    plt.figure(figsize=(8, 4))
    plt.pcolormesh(times, frequencies, np.log10(spectrogram), shading='auto', cmap='inferno')
    plt.xlim(0,1)
    plt.colorbar(label='Power Spectral Density (dB)')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.title(f'Time-Frequency Representation - Signal {i+1}')
    plt.tight_layout()
    plt.savefig(os.path.join(directory2, f'signal_{i+1}_time_frequency.png'), format='png')
    plt.close()
