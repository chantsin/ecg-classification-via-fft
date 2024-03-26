import wfdb
import numpy as np

def load_signal(path, metadata):
    """Loads whole ECG data set. Provide the path and metadata file.
    
    Examples
    --------
    >>> X, y = load_signal('../data/physionet.org/files/ptb-xl/1.0.3/', metadata)
    >>> X.shape, y.shape
    ((100, 3), (100,))
    """
    signals = [wfdb.rdsamp(path + temp_path) for temp_path in metadata['filename_hr']]
    X_data = np.array([signal for signal, fields in signals])
    y_data = metadata['diagnostic_superclass']
    
    return X_data, y_data

def load_sample_signal(sample_size, path, metadata, freq='low'):
    """Loads a sample of the ECG data set. 
    
    Sample size is the amount of random rows to take from you data and can be 
    set depending on user needs. Option to look at high frequency data as well 
    (5000 sample points), default is low (1000 sample points).

    Examples
    --------
    >>> X_sample, y_sample = load_sample_signal(1000, path, metadata)
    >>> X_sample.shape, y_sample.shape
    ((1000, 3), (1000,))
    """
    metadata = metadata.sample(sample_size)

    if freq == 'high':
        signals = [wfdb.rdsamp(path + temp_path) for temp_path in metadata['filename_hr']]
    else: 
        signals = [wfdb.rdsamp(path + temp_path) for temp_path in metadata['filename_lr']]
    X_data = np.array([signal for signal, fields in signals])
    y_data = metadata['diagnostic_superclass']

    return X_data, y_data