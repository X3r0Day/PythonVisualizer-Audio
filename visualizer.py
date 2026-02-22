import wave
import numpy as np
import matplotlib.pyplot as plt


with open("song.wav", "rb") as wave_file:
    wave_obj = wave.open(wave_file)
    sample_freq = wave_obj.getframerate()
    n_samples = wave_obj.getnframes()
    t_audio = n_samples / sample_freq
    n_channels = wave_obj.getnchannels()

    signal_wave = wave_obj.readframes(n_samples)
    signal_array = np.frombuffer(signal_wave, dtype=np.int16)

    l_channel = signal_array[0::2]
    r_channel = signal_array[1::2]
    
    times = np.linspace(0, t_audio, num=n_samples)

    # Plotting Signal Amplitude of Left Channel
    plt.figure(figsize=(15,5))
    plt.plot(times, l_channel)
    plt.title("Left Channel")
    plt.ylabel("Signal Value")
    plt.xlabel("Time (s)")
    plt.xlim(0, t_audio)
    plt.show()

    # Plotting Frequency Spectrum of Left Channel
    plt.figure(figsize=(15,5))
    plt.specgram(l_channel, Fs=sample_freq, vmin=20, vmax=50)
    plt.title("Frequency Spectrum of Left Channel")
    plt.ylabel("Frequency (Hz)")
    plt.xlabel("Time (s)")
    plt.xlim(0, t_audio)
    plt.ylim(0, sample_freq)
    plt.colorbar(label="Intensity (dB)")
    plt.show()

    print("Sample Frequency:",sample_freq)  
    print("Number of Samples:",n_samples)
    print("Audio Length in Minutes:",t_audio/60)
    print("Number of Channels:",n_channels)
    print("Signal Wave Type:",type(signal_array))
    


    
