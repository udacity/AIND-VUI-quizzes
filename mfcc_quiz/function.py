from python_speech_features import mfcc
import scipy.io.wavfile as wav


def wav_to_mfcc(wav_filename):
    """ extract MFCC features from a wav file

    :param wav_filename: filename with .wav format
    :return: MFCC features for wav file
    """

    # TODO implement
    return None


if __name__ == '__main__':
    import mfcc_quiz.dutils
    mfcc_sig = wav_to_mfcc('nd889_audio/sample02.wav')
    (rate, raw_sig) = wav.read('nd889_audio/sample02.wav')
    mfcc_quiz.dutils.plot_raw_audio(raw_sig)
    mfcc_quiz.dutils.plot_mfcc_feature(mfcc_sig)


