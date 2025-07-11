# visualize_utils.py

import os
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

def plot_waveform(file_path, output_dir="graphs"):
    y, sr = sf.read(file_path)
    if y.ndim > 1:
        y = np.mean(y, axis=1)  # convert to mono if stereo

    time = np.linspace(0, len(y) / sr, num=len(y))

    plt.figure(figsize=(10, 4))
    plt.plot(time, y, color='purple')
    plt.title(f"Waveform: {os.path.basename(file_path)}")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.tight_layout()

    # Save plot
    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, os.path.splitext(os.path.basename(file_path))[0] + "_waveform.png")
    plt.savefig(out_path)
    plt.show()

    return out_path
