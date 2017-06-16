# runs when student click "test"
import q1_function as function
import q1_utils as utils
import matplotlib.pyplot as plt

freqs = function.choose_frequencies()
num_samples, spacing, t = utils.get_wave_timing()
# function.demo_fft(num_samples, spacing, t)

if len(freqs) == 3 and max(freqs)<=50 and min(freqs)>=1:
    print('Frequencies look good!')
    wave1 = utils.sinusoid(t * freqs[0])
    wave2 = utils.sinusoid(t * freqs[1])
    wave3 = utils.sinusoid(t * freqs[2])
    sum_waves = wave1 + wave2 + wave3
    plt.plot = utils.display_sinusoids(t, wave1, wave2, wave3, sum_waves)
    plt.show()

else:
    print('Something is wrong with the frequencies...')
    print('...there should be three with a range between 1 and 50,')
    print('but the result was {}'.format(freqs))
