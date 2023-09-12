import numpy as np

def generate_ca_signals(num_signals,num_samples, duration,signal_type=0):
    
    signals=[]
    #noise limit
    noise_level = noise_level = 0.5  # Maximum noise level
    # Generate time axis
    time = np.linspace(0, duration, num_samples)
    rise_time = 0.01  # Time taken for spike to rise
    
    
    for _ in range(num_signals):
        # Generate noise
        noise = np.random.uniform(0, noise_level, num_samples)
        # Generate spike waveform
        spike_waveform = np.zeros(num_samples)
        
        if signal_type==0:
            
            spike_locations = [int(np.random.uniform(0.1, 0.3)*num_samples), int(np.random.uniform(0.5, 0.7)*num_samples)]  # Locations of the spikes
            

            for location in spike_locations:
                spike_amplitude = np.random.uniform(5.0, 10.0)
                decay_time = np.random.uniform(0.1, 0.3)
                spike_waveform[location+1:int(location+rise_time*num_samples)] += np.linspace(0, spike_amplitude, int(rise_time*num_samples)-1)
                # Exponential decay
                decay_samples = int((decay_time - rise_time) * num_samples)
                decay_range = np.linspace(spike_amplitude, 0, decay_samples)
                decay_factor = np.exp(-2.75 * np.linspace(0, 5, decay_samples))  # Exponential decay factor
                spike_waveform[int(location+rise_time*num_samples):int(location+decay_time*num_samples)] += decay_range * decay_factor
            
            
    
                # Combine noise and spike waveform
            signals.append(noise + spike_waveform)
                
                
        if signal_type==1:
            location = int(np.random.uniform(0.5, 0.65)*num_samples)  # Locations of the spikes
            spike_amplitude = np.random.uniform(5.0, 10.0)
            decay_time = np.random.uniform( 0.1, 0.35)
            spike_waveform[location+1:int(location+rise_time*num_samples)] += np.linspace(0, spike_amplitude, int(rise_time*num_samples)-1)
            # Exponential decay
            decay_samples = int((decay_time - rise_time) * num_samples)
            decay_range = np.linspace(spike_amplitude, 0, decay_samples)
            decay_factor = np.exp(-2.75 * np.linspace(0, 5, decay_samples))  # Exponential decay factor
            spike_waveform[int(location+rise_time*num_samples):int(location+decay_time*num_samples)] += decay_range * decay_factor
            
            
    
                # Combine noise and spike waveform
            signals.append(noise + spike_waveform)
            
    return signals,time
