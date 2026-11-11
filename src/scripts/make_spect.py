from language_detection.spect import main
from language_detection.data.spectrogram.functions import compute_lowpass_spectrogram_batch, compute_spectrogram_batch

if __name__ == '__main__':
    languages = ["de", "en", "es", "it", "ja", "nl", "ta"]

    n_ftt = 1024
    hop_length = 512
    sr = 16_000

    entry = {"sr": sr, "n_fft": n_ftt, "hop_length": hop_length, "spect_f" : compute_spectrogram_batch}

    main(languages, entry)