import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack
import q1_utils as utils

def choose_frequencies():
    # pick three frequencies in a range between 0 and 50
    # they will be given random amplitudes and phases
    # *** TODO provide three frequencies between 1 and 50
    freq1 = 3
    freq2 = 8
    freq3 = 1
    return(freq1, freq2, freq3)


def demo_fft(num_samples, spacing, t):

    w1, w2, w3 = utils.make_waves(choose_frequencies())
    sum_waves = w1+w2+w3

    yf = scipy.fftpack.fft(sum_waves)
    # only show half
    xf = np.linspace(0.0, 1.0 / (2.0 * spacing), num_samples / 2)
    utils.display_fft(xf, yf)

if __name__ == '__main__':
    num_samples, spacing, t = utils.get_wave_timing()
    demo_fft(num_samples, spacing, t)