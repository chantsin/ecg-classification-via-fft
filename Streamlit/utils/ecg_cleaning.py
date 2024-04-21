import numpy as np
import wfdb 

def baseline_removal(sig, freq_start, freq_stop, signal_samp_freq='low'):
    """This function will zero low frequency noise given an ECG signal using 
    Fourier Transforms (specifically baseline wandering). 
    
    When a specific start frequency is defined, by default it will zero that 
    frequency and frequencies higher unless the upper bound is specified. 
    
    The signals default sampling frequency is also set to 'low', meaning a 
    sampling frequency of 100 Hz, otherwise it can be set to 'high', meaning a 
    sampling frequency of 500 Hz.

    """
    sig = np.array(sig)
    
    ##### PARAMETER SETTING
    
    # High Frequency Parameters
    if signal_samp_freq == 'high':
        sampling_freq = 500
        sig_len = 5000
    else: 
        # Low Frequency Parameters
        sampling_freq = 100
        sig_len = 1000
    
    # Set up stepsize 
    dt = 1/sampling_freq
    
    # Flatten the signal from 2D to 1D 
    sigs = sig.flatten()
    
    ##### FFT SIGNAL
    
    # FFT returns a result not centered at zero, therefore we need to fftshift it to zero
    sig_fft = np.fft.fftshift(np.fft.fft(sigs) * dt)
    freq = np.fft.fftshift(np.fft.fftfreq(sig_len, dt))
    
    ##### BASELINE REMOVAL 
    for i in range(len(freq)):
        
        # Setting positive frequencies to zero
        if (freq[i] >= freq_start) & (freq[i] <= freq_stop):

            sig_fft[i] = 0

        # Setting negative frequencies to zero
        elif (freq[i] >= -freq_stop) & (freq[i] <= -freq_start):

            # Set negative frequencies to zero 
            sig_fft[i] = 0
    
    ##### IFFT SIGNAL
    
    new_signal = np.fft.ifft(np.fft.ifftshift(sig_fft)) / dt
    
    return np.real(new_signal)


def high_freq_removal(sig, freq_start, freq_stop=None, signal_samp_freq='low'):
    """This function will zero high frequency noise given an ECG signal using 
    Fourier Transforms. 
    
    When a specific start frequency is defined, by default it will zero that 
    frequency and frequencies higher unless the upper bound is specified. 
    
    The signals default sampling frequency is also set to 'low', meaning a 
    sampling frequency of 100 Hz, otherwise it can be set to 'high', meaning a 
    sampling frequency of 500 Hz. 

    """
    sig = np.array(sig)
    
    ##### PARAMETER SETTING
    
    # High Frequency Parameters
    if signal_samp_freq == 'high':
        sampling_freq = 500
        sig_len = 5000
    else: 
        # Low Frequency Parameters
        sampling_freq = 100
        sig_len = 1000
        
    # Set stepsize 
    dt = 1/sampling_freq
    
    # Flatten the signal from 2D to 1D 
    sigs = sig.flatten()
    
    ##### FFT SIGNAL
    
    # FFT returns a result not centered at zero, therefore we need to fftshift it to zero
    sig_fft = np.fft.fftshift(np.fft.fft(sigs) * dt)
    freq = np.fft.fftshift(np.fft.fftfreq(sig_len, dt))
    
    # Override stopping frequency if specified
    if freq_stop == None:
        freq_stop = freq[-1]
    else: 
        freq_stop = freq_stop

    ##### HIGH FREQUENCY REMOVAL 
    for i in range(len(freq)):
        
        # Setting positive frequencies to zero
        if (freq[i] >= freq_start) & (freq[i] <= freq_stop):
 
            sig_fft[i] = 0

        # Setting negative frequencies to zero
        elif (freq[i] >= -freq_stop) & (freq[i] <= -freq_start):

            sig_fft[i] = 0
    
    ##### IFFT SIGNAL
    
    new_sig = np.fft.ifft(np.fft.ifftshift(sig_fft)) / dt
    
    return np.real(new_sig)

def grab_sample(age, sex, path, metadata):
    
    metadata = metadata[metadata['age'] == age]
    metadata = metadata[metadata['sex'] == sex]
    #metadata = metadata[metadata['height'] == height]
    #metadata = metadata[metadata['weight'] == weight]
    
    if metadata.shape[0] == 0:
        print("No sample ECG with these attributes!")
    else:
        temp_path = metadata.sample()['filename_lr'].iloc[0]
    
        signals = wfdb.rdsamp(path + temp_path, channels=[1])
        X_data = np.array(signals[0])
    
        return X_data