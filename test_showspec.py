import os
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
import soundfile as sf

# Function to show magnitude spectrogram with a specific colormap
def show_magspec(waveform, cmap='viridis', **kw):
    return librosa.display.specshow(
        librosa.amplitude_to_db(np.abs(librosa.stft(waveform)), ref=np.max),
        y_axis="hz", x_axis="time",
        cmap=cmap,  # 设置颜色映射
        **kw
    )
filepath = 'E:/168数据/202307301558-1609/1/output_audio_0730160812.wav'
waveform = sf.read(filepath)[0]

# Create a plot for the waveform with a specific colormap
plt.figure(figsize=(7, 5))
plt.ylim(10000, 16000)
plt.xlim(0, 30)
show_magspec(waveform, cmap='viridis', sr=125000)
plt.colorbar(format="%+2.0f dB")
plt.show()