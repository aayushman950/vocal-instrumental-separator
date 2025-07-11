# 🎵 Vocal & Instrumental Separator (DSP Project)

This Python project separates vocals and instrumentals from `.wav` audio files using **Digital Signal Processing (DSP)** techniques. It features:

- A **manual STFT-based method** using SciPy
- A **Librosa-based method** for enhanced separation
- A user-friendly **GUI** built with Tkinter
- Automatic **waveform visualization**

## 🔧 Requirements

- Python 3.8+
- Libraries:
  - `librosa`
  - `scipy`
  - `numpy`
  - `soundfile`
  - `pygame`
  - `matplotlib`
  - `tkinter`

Install with:

```bash
pip install -r requirements.txt
```

🚀 How to Run
Clone the Repository

```bash
git clone https://github.com/aayushman950/vocal-instrumental-separator.git
cd vocal-instrumental-separator
```

Run the application
```bash
python main.py
```

# How to Use

- Click **"Add Song"** to load a `.wav` file into the app.  
- Click on the song in the list.  
- Use **Play**, **Pause**, and **Stop** to control playback.  
- Click **"Extract"** to generate:  
  - `*_vocals.wav` and `*_instrumentals.wav`  
  - These files are saved in the `/output/` folder.  

## 📊 Waveform Visualization

Waveform plots are automatically saved as images for:  
- Original audio  
- Extracted vocals  
- Extracted instrumentals  

You can find these images in the `/graphs/` directory.  

## 🎧 Sample Outputs

The input and output `.wav` files, including examples extracted using both manual and Librosa methods, are available in the `/output/` directory.
