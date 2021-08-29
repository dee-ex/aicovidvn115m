import pandas as pd
import numpy as np

from sklearn.preprocessing import MinMaxScaler

# ==============================================================================

def scale(x, x_private):
    scaler = MinMaxScaler()
    scaler.fit(x)

    print(scaler.data_max_)
    print(scaler.data_min_)

    nor_x = scaler.transform(x)
    nor_x_private = scaler.transform(x_private)

    return nor_x, nor_x_private

def save(x, nonnor_label, df, path):
    _df = pd.DataFrame(x)
    _df[nonnor_label] = df[nonnor_label]

    _df.to_csv(path, index=False)

# ==============================================================================

def normalize():
    mfcc = pd.read_csv("../data/train_features/mfcc_features.csv")
    chroma = pd.read_csv("../data/train_features/chroma_features.csv")
    mel = pd.read_csv("../data/train_features/mel_features.csv")
    zcr = pd.read_csv("../data/train_features/zcr_features.csv")

    mfcc_private = pd.read_csv("../data/private_features/mfcc_features.csv")
    chroma_private = pd.read_csv("../data/private_features/chroma_features.csv")
    mel_private = pd.read_csv("../data/private_features/mel_features.csv")
    zcr_private = pd.read_csv("../data/private_features/zcr_features.csv")

    # ==============================================================================

    raw_mfcc = mfcc.iloc[:, :-1]
    raw_mfcc_private = mfcc_private.iloc[:, :-1]

    raw_chroma = chroma.iloc[:, :-1]
    raw_chroma_private = chroma_private.iloc[:, :-1]

    raw_mel = mel.iloc[:, :-1]
    raw_mel_private = mel_private.iloc[:, :-1]

    raw_zcr = zcr.iloc[:, :-1]
    raw_zcr_private = zcr_private.iloc[:, :-1]

    # ==============================================================================

    nor_mfcc, nor_mfcc_private = scale(raw_mfcc, raw_mfcc_private)
    nor_chroma, nor_chroma_private = scale(raw_chroma, raw_chroma_private)
    nor_mel, nor_mel_private = scale(raw_mel, raw_mel_private)
    nor_zcr, nor_zcr_private = scale(raw_zcr, raw_zcr_private)

    # ==============================================================================

    save(nor_mfcc, "label", mfcc, "../data/train_features/minmax_mfcc_features.csv")
    save(nor_mfcc_private, "uuid", mfcc_private, "../data/private_features/minmax_mfcc_features.csv")

    save(nor_chroma, "label", chroma, "../data/train_features/minmax_chroma_features.csv")
    save(nor_chroma_private, "uuid", chroma_private, "../data/private_features/minmax_chroma_features.csv")

    save(nor_mel, "label", mel, "../data/train_features/minmax_mel_features.csv")
    save(nor_mel_private, "uuid", mel_private, "../data/private_features/minmax_mel_features.csv")

    save(nor_zcr, "label", zcr, "../data/train_features/minmax_zcr_features.csv")
    save(nor_zcr_private, "uuid", zcr_private, "../data/private_features/minmax_zcr_features.csv")

if __name__ == "__main__":
    normalize()
