import pytest
import numpy as np

from freqtag import psd_from_mne_epochs


@pytest.fixture
def tutorial_epochs():
    import mne

    # Load raw data
    data_path = mne.datasets.ssvep.data_path()
    bids_fname = (data_path +
                  '/sub-02/ses-01/eeg/sub-02_ses-01_task-ssvep_eeg.vhdr')

    raw = mne.io.read_raw_brainvision(bids_fname, preload=True, verbose=False)
    raw.info['line_freq'] = 50.

    # Set montage
    montage = mne.channels.make_standard_montage('easycap-M1')
    raw.set_montage(montage, verbose=False)

    # Set common average reference
    raw.set_eeg_reference('average', projection=False, verbose=False)

    # Apply bandpass filter
    raw.filter(l_freq=0.1, h_freq=None, fir_design='firwin', verbose=False)

    # Construct epochs
    event_id = {
        '12hz': 255,
        '15hz': 155
    }
    events, _ = mne.events_from_annotations(raw, verbose=False)
    raw.info["events"] = events
    tmin, tmax = -1., 20.  # in s
    baseline = None

    return mne.Epochs(
        raw, events=events,
        event_id=[event_id['12hz'], event_id['15hz']], tmin=tmin,
        tmax=tmax, baseline=baseline, verbose=False)


@pytest.fixture
def tutorial_spectrum(tutorial_epochs):
    import mne

    tmin = 1.
    tmax = 20.
    fmin = 1.
    fmax = 90.
    sfreq = tutorial_epochs.info['sfreq']

    psds, freqs = mne.time_frequency.psd_welch(
        tutorial_epochs,
        n_fft=int(sfreq * (tmax - tmin)),
        n_overlap=0, n_per_seg=None,
        tmin=tmin, tmax=tmax,
        fmin=fmin, fmax=fmax,
        window='boxcar',
        verbose=False)

    return psds, freqs


def test_from_mne_epochs(tutorial_spectrum, tutorial_epochs):
    psds, freqs = tutorial_spectrum
    spectrum = psd_from_mne_epochs(tutorial_epochs, tmin=1., tmax=20.,
                                   fmin=1., fmax=90.)

    assert np.allclose(spectrum.data, psds)
    assert np.allclose(spectrum.frequencies, freqs)
