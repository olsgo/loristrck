import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from . import util

def load_audio_file(file_path):
    sr, audio_data = wavfile.read(file_path)
    return audio_data, sr

def save_audio_file(audio_data, sr, file_path):
    wavfile.write(file_path, sr, audio_data)

def visualize_waveform(audio_data, sr, ax=None):
    if ax is None:
        ax = plt.gca()
    time = np.arange(len(audio_data)) / sr
    ax.plot(time, audio_data)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Amplitude')
    ax.set_title('Waveform')
    return ax

def visualize_spectrogram(audio_data, sr, ax=None):
    if ax is None:
        ax = plt.gca()
    ax.specgram(audio_data, Fs=sr)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Frequency (Hz)')
    ax.set_title('Spectrogram')
    return ax

def visualize_partial_tracking(partials, ax=None):
    if ax is None:
        ax = plt.gca()
    util.plot_partials(partials, ax=ax)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Frequency (Hz)')
    ax.set_title('Partial Tracking')
    return ax

def apply_time_stretch(partials, factor):
    return util.partials_stretch(partials, factor)

def apply_frequency_shift(partials, shift):
    return util.partials_transpose(partials, shift)

def apply_harmonic_remap(partials, mapping):
    return util.partials_transpose(partials, mapping)
