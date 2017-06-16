import matplotlib.pyplot as plt
# import plotly.plotly as py
import numpy as np
from numpy import fft
import scipy.fftpack


# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

def canned():
    # from https://plot.ly/matplotlib/fft/
    Fs = 150.0  # sampling rate
    Ts = 1.0/Fs # sampling interval
    t = np.arange(0,1,Ts) # time vector

    ff = 5   # frequency of the signal
    y = np.sin(2*np.pi*ff*t)

    n = len(y) # length of the signal
    k = np.arange(n)
    T = n/Fs
    frq = k/T # two sides frequency range
    frq = frq[range(int(n/2))] # one side frequency range

    Y = np.fft.fft(y)/n # fft computing and normalization
    Y = Y[range(int(n/2))]

    fig, ax = plt.subplots(2, 1)
    ax[0].plot(t,y)
    ax[0].set_xlabel('Time')
    ax[0].set_ylabel('Amplitude')
    ax[1].plot(frq,abs(Y),'r') # plotting the spectrum
    ax[1].set_xlabel('Freq (Hz)')
    ax[1].set_ylabel('|Y(freq)|')

    plot_url = py.plot_mpl(fig, filename='mpl-basic-fft')

def canned2():
    # http://snowball.millersville.edu/~adecaria/ESCI386P/esci386-lesson17-Fourier-Transforms.pdf
    from numpy import fft
    import numpy as np
    import matplotlib.pyplot as plt
    n = 1000  # Number of data points
    dx = 5.0  # Sampling period (in meters)
    x = dx * np.arange(0, n)  # x coordinates
    w1 = 100.0  # wavelength (meters)
    w2 = 20.0  # wavelength (meters)
    fx = np.sin(2 * np.pi * x / w1) + 2 * np.cos(2 * np.pi * x / w2)  # signal
    Fk = fft.fft(fx) / n  # Fourier coefficients (divided by n)
    nu = fft.fftfreq(n, dx)  # Natural frequencies
    Fk = fft.fftshift(Fk)  # Shift zero freq to center
    nu = fft.fftshift(nu)  # Shift zero freq to center
    f, ax = plt.subplots(3, 1, sharex=True)
    ax[0].plot(nu, np.real(Fk))  # Plot Cosine terms
    ax[0].set_ylabel(r'$Re[F_k]$', size='x-large')
    ax[1].plot(nu, np.imag(Fk))  # Plot Sine terms
    ax[1].set_ylabel(r'$Im[F_k]$', size='x-large')
    ax[2].plot(nu, np.absolute(Fk) ** 2)  # Plot spectral power
    ax[2].set_ylabel(r'$\vert F_k \vert ^2$', size='x-large')
    ax[2].set_xlabel(r'$\widetilde{\nu}$', size='x-large')
    plt.show()

def canned3():

    import numpy as np
    import matplotlib.pyplot as plt
    import scipy.fftpack

    # Number of samplepoints
    N = 600
    # sample spacing
    T = 1.0 / 800.0
    x = np.linspace(0.0, N * T, N)
    y = np.sin(50.0 * 2.0 * np.pi * x) + 0.5 * np.sin(80.0 * 2.0 * np.pi * x)
    yf = scipy.fftpack.fft(y)
    xf = np.linspace(0.0, 1.0 / (2.0 * T), N / 2)

    fig, ax = plt.subplots()
    ax.plot(xf, 2.0 / N * np.abs(yf[:N // 2]))
    plt.show()


def show_three_sinusoids(freq1, freq2, freq3):
    def sinusoid(freq):
        phase = 0.3
        return np.cos(2*np.pi * freq - phase)
    # Number of sample points per T=1
    N = 500
    # Time range to display
    R = 5.0
    # sample period
    T = R / N

    t = np.arange(0.0, R, T) # returns an array of evenly spaced values

    # plot three frequencies with random phase shifts
    plt.figure(1)
    f1 = sinusoid(t*freq1)
    f2 = sinusoid(t*freq2)
    f3 = sinusoid(t*freq3)
    f4 = f1+f2+f3

    plt.subplot(411) #3 rows, 1 column, fignum 1
    plt.plot(t, f1)
    plt.title('1st frequency component')

    plt.subplot(412) #3 rows, 1 column, fignum 2
    plt.plot(t, f2)
    plt.title('2nd frequency component')


    plt.subplot(413) #3 rows, 1 column, fignum 3
    plt.plot(t, f3)
    plt.title('3rd frequency component')


    # sum
    plt.subplot(414) #3 rows, 1 column, fignum 4
    plt.plot(t, f4, 'r')
    plt.title('Sum of components')

    # adjust format of display to make room for titles
    plt.subplots_adjust(
        top=0.94,
        bottom=0.06,
        left=0.09,
        right=0.97,
        hspace=0.65,
        wspace=0.2
        )
    plt.show()
    return f4

def splitem(freq_max, signal):

    # Number of sample points per T=1
    N = np.shape(signal)[0]
    # Frequency range to display
    R = 5.0
    # sample period
    T = R / N
    print('T={}'.format(T))
    print('linspace end = {}'.format(1.0/(2.0*T)))

    yf = scipy.fftpack.fft(signal)
    # start, stop, number of samples
    xf = np.linspace(0.0, 1.0 / (2.0 * T), N / 2)

    fig, ax = plt.subplots()
    ax.plot(xf, 2.0 / N * np.abs(yf[:N // 2]))
    plt.show()


if __name__ == '__main__':


    # pick three frequencies and add them
    f1 = 3
    f2 = 9
    f3 = 13

    fsum= show_three_sinusoids(f1, f2, f3)

    # now decompose
    splitem(max(f1, f2, f3), fsum)