from math import ceil

import numpy as np


class Spectrum(object):
    def __init__(self, data, frequencies, kind):
        self.data = data
        self.frequencies = frequencies
        self.kind = kind

    @classmethod
    def psd_from_mne_epochs(cls, epochs, tmin=0, tmax=np.inf, fmin=0,
                            fmax=np.inf) -> 'Spectrum':
        """
        Applies Fourier transform to data in an mne.Epochs object and
        calculates power spectral density.

        :param epochs: mne.Epochs object
        :param tmin: minimum time of interest
        :param tmax: maximum time of interest (the sample at this time is not
         included)
        :param fmin: minimum frequency of interest
        :param fmax: maximum frequency of interest
        :return: an object of type Spectrum
        """
        # Prepare data
        data = epochs.get_data()
        time_mask = (tmin <= epochs.times) & (epochs.times < tmax)

        # Fourier
        n_fft = int(epochs.info['sfreq'] * (tmax - tmin))
        F = np.fft.rfft(data[..., time_mask], axis=-1, norm='ortho')

        # Calculate power
        power = np.abs(F) ** 2
        # power at avery frequency but the DC and Nyqvist should be multiplied
        # by two
        nyqvist_index = ceil(n_fft / 2)
        power[1:nyqvist_index] *= 2

        # We are calculating "density" so we need to convert power to "1/Hz"
        # units.
        psd = power / epochs.info['sfreq']

        # Calculate frequencies and remove the unnecessary ones
        frequencies = np.fft.rfftfreq(n=n_fft, d=(1 / epochs.info['sfreq']))
        frequency_mask = (fmin <= frequencies) & (frequencies <= fmax)
        psd = psd[..., frequency_mask]
        frequencies = frequencies[frequency_mask]

        return cls(data=psd, frequencies=frequencies, kind='psd')
