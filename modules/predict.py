import os
import pickle
import numpy as np
import pandas as pd
import lightgbm as lgbm

def prepare():
    mfcc_private = pd.read_csv("../data/private_features/minmax_mfcc_features.csv")
    chroma_private = pd.read_csv("../data/private_features/minmax_chroma_features.csv")
    mel_private = pd.read_csv("../data/private_features/minmax_mel_features.csv")
    zcr_private = pd.read_csv("../data/private_features/minmax_zcr_features.csv")

    test_df = pd.concat([zcr_private.iloc[:, :-1],
                        mfcc_private.iloc[:, :-1],
                        chroma_private.iloc[:, :-1], mel_private], axis=1)

    X_test = test_df.iloc[:, :-1].values

    print(X_test.shape)

    return X_test, test_df

def predict():
    X_test, test_df = prepare()

    res = np.zeros(X_test.shape[0])

    model_list = os.listdir("../weights/models/")

    for name in model_list:
        model = pickle.load(open("../weights/models/" + name, "rb"))

        res += model.predict(X_test)

    res /= len(model_list)

    submission = pd.DataFrame()
    submission["uuid"] = test_df["uuid"]
    submission["assessment_result"] = res
    submission.to_csv("results.csv", index=0)

if __name__ == "__main__":
    predict()
