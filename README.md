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
  - `tkinter` *(built-in)*

Install with:

```bash
pip install -r requirements.txt

🚀 How to Run
Clone the Repository

bash
Copy
Edit
git clone https://github.com/your-username/vocal-instrumental-separator.git
cd vocal-instrumental-separator
Run the Application

bash
Copy
Edit
python main.py
🧪 How to Use
Click "Add Song" to load a .wav file into the app.

Use Play, Pause, and Stop to control playback.

Click "Extract" to generate:

*_vocals.wav and *_instrumentals.wav

Saved in the /output/ folder

Waveforms are saved in the /graphs/ folder.

📊 Waveform Visualization
Waveform plots are automatically saved as images for:

Original audio

Extracted vocals

Extracted instrumentals

You can find these in the /graphs/ directory.

🎧 Sample Outputs
The input and output .wav files, including examples extracted using both manual and Librosa methods, are available here:

🔗 GitHub Output Folder

⚙️ Git Ignore
The .gitignore includes:

gitignore
Copy
Edit
__pycache__/
*.pyc
To remove previously committed __pycache__:

bash
Copy
Edit
git rm -r --cached __pycache__/
git commit -m "Remove pycache from repo"
git push