import numpy as np
from scipy.signal import convolve
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Read the audio file
sample_rate, audio_data = wavfile.read("C:\\Users\\walt314\\Downloads\\input.wav") 
print(audio_data.shape)

# Set the window size for the moving average
window_size = 51  # Must be odd

# Mean filter
kernel = np.ones(window_size) / window_size
mean_filtered = np.zeros_like(audio_data)  # Create an empty array to store the filtered data

# To filter each channel of the audio data
for channel in range(audio_data.shape[1]):
    mean_filtered[:, channel] = convolve(audio_data[:, channel], kernel, mode='same')

# Draw audio data plots
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.title("Original audio")
plt.plot(audio_data)

plt.subplot(2, 1, 2)
plt.title("Mean filtered audio")
plt.plot(mean_filtered)

# Save the filtered audio
wavfile.write("C:\\Users\\walt314\\Downloads\\mean_filtered.wav", sample_rate, mean_filtered)

plt.tight_layout()
plt.show()
plt.savefig("C:\\Users\\walt314\\Downloads\\mean_filtered.png")