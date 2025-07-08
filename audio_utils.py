import numpy as np
import soundfile as sf
import os
from scipy.signal import stft, istft
from scipy.ndimage import median_filter

def load_audio(file_path):
    y, sr = sf.read(file_path)
    if y.ndim > 1:
        y = np.mean(y, axis=1)  # convert to mono if stereo
    return y, sr

def softmask(X, X_ref, power=2):
    """Compute a soft mask for source separation"""
    X = np.maximum(X, 1e-10)
    X_ref = np.maximum(X_ref, 1e-10)
    return (X ** power) / (X ** power + X_ref ** power)

def extract_vocals_instrumentals(file_path):
    y, sr = load_audio(file_path)

    # Parameters
    n_fft = 2048
    hop_length = n_fft // 4

    # STFT
    f, t, Zxx = stft(y, fs=sr, nperseg=n_fft, noverlap=n_fft - hop_length)
    S_full = np.abs(Zxx)
    phase = np.exp(1j * np.angle(Zxx))

    # Spectral filtering using median filtering
    S_filter = median_filter(S_full, size=(1, 15))  # median over time (31 frames ~ 2s)

    # Masking
    margin_i, margin_v = 2, 10
    power = 2

    mask_i = softmask(S_filter, margin_i * (S_full - S_filter), power=power)
    mask_v = softmask(S_full - S_filter, margin_v * S_filter, power=power)

    S_foreground = mask_v * S_full
    S_background = mask_i * S_full

    # Reconstruct complex spectrograms
    Zxx_fore = S_foreground * phase
    Zxx_back = S_background * phase

    # ISTFT
    _, y_foreground = istft(Zxx_fore, fs=sr, nperseg=n_fft, noverlap=n_fft - hop_length)
    _, y_background = istft(Zxx_back, fs=sr, nperseg=n_fft, noverlap=n_fft - hop_length)

    # Save output
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    base_filename = os.path.splitext(os.path.basename(file_path))[0]
    vocal_path = os.path.join(output_dir, f"{base_filename}_vocals.wav")
    instr_path = os.path.join(output_dir, f"{base_filename}_instrumentals.wav")

    sf.write(vocal_path, y_foreground, sr)
    sf.write(instr_path, y_background, sr)

    return vocal_path, instr_path