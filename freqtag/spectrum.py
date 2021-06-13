import numpy as np


class Spectrum(object):
    def __init__(self, data, frequencies, kind):
        self.data = data
        self.frequencies = frequencies
        self.kind = kind

    @classmethod
    def from_mne_epochs(cls, epochs, tmin=0, tmax=np.inf, fmin=0,
                        fmax=np.inf) -> 'Spectrum':
        """
        Applies Fourier transform to data in an mne.Epochs object.

        :param epochs: mne.Epochs object
        :param tmin: minimum time of interest
        :param tmax: maximum time of interest
        :param fmin: minimum frequency of interest
        :param fmax: maximum frequency of interest
        :return: an object of type Spectrum
        """
        from mne.time_frequency import psd_welch

        n_fft = int(epochs.info['sfreq'] * (tmax - tmin))
        power, frequencies = psd_welch(
            epochs,
            tmin=tmin, tmax=tmax,
            fmin=fmin, fmax=fmax,
            # These result in plain FFT: single window, no windowing function
            n_fft=n_fft, n_overlap=0, n_per_seg=None, window='boxcar',
            verbose=False)

        return cls(data=power, frequencies=frequencies, kind='power')
