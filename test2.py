import numpy as np
import matplotlib.pyplot as plt

# File path to your .iq file
iq_file_path = 'ads-b.iq'  # Replace with the actual path

# Specify the data type. Common options are:
# np.complex64 (if data is stored as complex numbers)
# np.int16 (if data is stored as 16-bit integers for interleaved I/Q)
data_type = np.complex64  # Adjust based on your file format

# --- Adjust these parameters based on your recording ---
sample_rate = 2e6  # Example: 2.048 MHz (adjust according to your recording)
center_freq = 1090e6    # Example: 100 MHz (adjust according to your recording)

try:
    # Read the IQ data from the file
    samples = np.fromfile(iq_file_path, dtype=data_type)

    # If your data is int16, convert to complex numbers:
    if data_type == np.int16:
        # Example conversion for interleaved I/Q (adjust if necessary)
        samples = samples.astype(np.float32)
        samples = samples[::2] + 1j * samples[1::2]
        # Optional: Normalize to -1 to +1
        samples /= 32768

    # Calculate and plot the spectrogram
    plt.figure(figsize=(10, 6))
    plt.specgram(samples, Fs=sample_rate, NFFT=1024, cmap='viridis') #
    plt.title('Spectrogram of IQ Data')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.colorbar(label='Intensity (dB)')
    plt.show()

except FileNotFoundError:
    print(f"Error: File not found at {iq_file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
