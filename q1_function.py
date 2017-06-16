import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack
from q1_utils import sinusoid, display_sinusoids, display_fft

def choose_frequencies():
    # pick three frequencies in a range between 0 and 50
    # they will be given random amplitudes and phases
    # *** TODO provide three frequencies between 1 and 50
    freq1 = 3
    freq2 = 8
    freq3 = 1
    return(freq1, freq2, freq3)

def demo_fft():
    # Number of sample points
    num_samples = 500
    # range max to display
    range_of_time = 5.0
    # sample spacing
    spacing = range_of_time/num_samples
    # array for time samples
    t = np.linspace(0.0, range_of_time, num_samples)

    freq1, freq2, freq3 = choose_frequencies()
    # create the sinusoidal waves and add them
    wave1 = sinusoid(t * freq1)
    wave2 = sinusoid(t * freq2)
    wave3 = sinusoid(t * freq3)
    sum_waves = wave1 + wave2 + wave3

    # display the waves
    thepictoshow = display_sinusoids(t, wave1,wave2,wave3, sum_waves)
    plt.plot = thepictoshow
    plt.show()

    yf = scipy.fftpack.fft(sum_waves)
    # only show half
    xf = np.linspace(0.0, 1.0 / (2.0 * spacing), num_samples / 2)
    display_fft(xf, yf)

if __name__ == '__main__':
    demo_fft()