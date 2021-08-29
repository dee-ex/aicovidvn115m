import librosa
import numpy as np
import pandas as pd

# ==============================================================================

def mean_feature(path):
    source, sr = librosa.load(path, res_type="kaiser_fast")
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

def extract_all(df):
    Xmfcc = []
    Xchroma = []
    Xmel = []
    Xzcr = []

    for path in df["path"]:
        mfcc, chroma, mel, zcr = mean_feature(path)

        Xmfcc.append(mfcc)
        Xchroma.append(chroma)
        Xmel.append(mel)
        Xzcr.append(zcr)

    return Xmfcc, Xchroma, Xmel, Xzcr

# ==============================================================================

def extract():
    train_df = pd.read_csv("../data/train.csv")
    private_df = pd.read_csv("../data/private.csv")

    Xmfcc, Xchroma, Xmel, Xzcr = extract_all(train_df)
    Xmfcc_private, Xchroma_private, Xmel_private, Xzcr_private = extract_all(private_df)

    # ==============================================================================

    mfcc_df = pd.DataFrame(Xmfcc)
    chroma_df = pd.DataFrame(Xchroma)
    mel_df = pd.DataFrame(Xmel)
    zcr_df = pd.DataFrame(Xzcr)

    mfcc_df["label"] = train_df["label"]
    chroma_df["label"] = train_df["label"]
    mel_df["label"] = train_df["label"]
    zcr_df["label"] = train_df["label"]

    mfcc_df.to_csv("../data/train_features/mfcc_features.csv", index=False)
    chroma_df.to_csv("../data/train_features/chroma_features.csv", index=False)
    mel_df.to_csv("../data/train_features/mel_features.csv", index=False)
    zcr_df.to_csv("../data/train_features/zcr_features.csv", index=False)

    # ==============================================================================

    mfcc_df_private = pd.DataFrame(Xmfcc_private)
    chroma_df_private = pd.DataFrame(Xchroma_private)
    mel_df_private = pd.DataFrame(Xmel_private)
    zcr_df_private = pd.DataFrame(Xzcr_private)

    mfcc_df_private["uuid"] = private_df["uuid"]
    chroma_df_private["uuid"] = private_df["uuid"]
    mel_df_private["uuid"] = private_df["uuid"]
    zcr_df_private["uuid"] = private_df["uuid"]

    mfcc_df_private.to_csv("private_features/mfcc_features.csv", index=False)
    chroma_df_private.to_csv("private_features/chroma_features.csv", index=False)
    mel_df_private.to_csv("private_features/mel_features.csv", index=False)
    zcr_df_private.to_csv("private_features/zcr_features.csv", index=False)

if __name__ == "__main__":
    extract()
