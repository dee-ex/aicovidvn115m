import os
import pickle
import joblib
import librosa
import numpy as np

def extract(file):
    source, sr = librosa.load(file, res_type="kaiser_fast")
    stft = np.abs(librosa.stft(source))

    mfcc = librosa.feature.mfcc(y=source, sr=sr, n_mfcc=13)
    chroma = librosa.feature.chroma_stft(S=stft, sr=sr)
    mel = librosa.feature.melspectrogram(y=source, sr=sr)
    zrc = librosa.feature.zero_crossing_rate(source)

    mfcc = np.mean(mfcc, axis=1)
    chroma = np.mean(chroma, axis=1)
    mel = np.mean(mel, axis=1)
    zcr = np.mean(zrc)

    return mfcc, chroma, mel, zcr

def scale(features, name):
    scaler = joblib.load(os.path.join(
                        os.path.dirname(os.path.dirname(__file__)),
                        f"weights/scalers/scaler_{name}.save"))

    return scaler.transform(features.reshape(1, -1))

def predict(file):

    mfcc, chroma, mel, zcr = extract(file)
    
    zcr = scale(zcr, "zcr").reshape(-1)
    mfcc = scale(mfcc, "mfcc").reshape(-1)
    chroma = scale(chroma, "chroma").reshape(-1)
    mel = scale(mel, "mel").reshape(-1)

    x = np.concatenate([zcr, mfcc, chroma, mel], axis=0).reshape(1, -1)

    res = 0

    model_list = os.listdir(os.path.join(
                            os.path.dirname(os.path.dirname(__file__)),
                            f"weights/models/"))

    for name in model_list:
        model = pickle.load(open(os.path.join(
                                os.path.dirname(os.path.dirname(__file__)),
                                f"weights/models/" + name), "rb"))

        res += model.predict(x)

    return (res /len(model_list))[0]
