import librosa
import librosa.display
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
import os

def load_audio_librosa(file_path):
    y, sr = librosa.load(file_path, sr=None, mono=True)
    return y, sr

def extract_vocals_instrumentals(file_path):
    y, sr = librosa.load(file_path, sr=None)
    S_full, phase = librosa.magphase(librosa.stft(y))

    S_filter = librosa.decompose.nn_filter(
        S_full,
        aggregate=np.median,
        metric='cosine',
        width=int(librosa.time_to_frames(2, sr=sr))
    )
    S_filter = np.minimum(S_full, S_filter)

    margin_i, margin_v = 2, 10
    power = 2

    mask_i = librosa.util.softmask(S_filter, margin_i * (S_full - S_filter), power=power)
    mask_v = librosa.util.softmask(S_full - S_filter, margin_v * S_filter, power=power)

    S_foreground = mask_v * S_full
    S_background = mask_i * S_full

    y_foreground = librosa.istft(S_foreground * phase)
    y_background = librosa.istft(S_background * phase)

    # Ensure output folder exists
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Construct output file paths
    base_filename = os.path.splitext(os.path.basename(file_path))[0]
    vocal_path = os.path.join(output_dir, f"{base_filename}_vocals.wav")
    instr_path = os.path.join(output_dir, f"{base_filename}_instrumentals.wav")

    sf.write(vocal_path, y_foreground, sr)
    sf.write(instr_path, y_background, sr)

    return vocal_path, instr_path