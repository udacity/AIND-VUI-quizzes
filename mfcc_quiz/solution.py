from python_speech_features import mfcc
import scipy.io.wavfile as wav


def wav_to_mfcc(wav_filename):
    """ extract MFCC features from a wav file
    
    :param wav_filename: filename with .wav format
    :return: MFCC features for wav file
    """
    (rate, sig) = wav.read(wav_filename)
    mfcc_features = mfcc(sig, rate, numcep=13)
    return mfcc_features


if __name__ == '__main__':
    import mfcc_quiz.dutils
    mfcc_sig = wav_to_mfcc('sample02.wav')
    (rate, raw_sig) = wav.read('sample02.wav')
    mfcc_quiz.dutils.plot_raw_audio(raw_sig)
    mfcc_quiz.dutils.plot_mfcc_feature(mfcc_sig)


