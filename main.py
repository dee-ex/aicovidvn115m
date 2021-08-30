import os
import pickle
import joblib
import argparse
import numpy as np
from modules import extract

def scale(features, name):
    scaler = joblib.load(f"weights/scalers/scaler_{name}.save")

    return scaler.transform(features.reshape(1, -1))

def predict(filename):

    mfcc, chroma, mel, zcr = extract.mean_feature(filename)
    
    zcr = scale(zcr, "zcr").reshape(-1)
    mfcc = scale(mfcc, "mfcc").reshape(-1)
    chroma = scale(chroma, "chroma").reshape(-1)
    mel = scale(mel, "mel").reshape(-1)

    x = np.concatenate([zcr, mfcc, chroma, mel], axis=0).reshape(1, -1)

    res = 0

    model_list = os.listdir("weights/models/")

    for name in model_list:
        model = pickle.load(open("weights/models/" + name, "rb"))

        res += model.predict(x)

    return (res /len(model_list))[0]

parser = argparse.ArgumentParser(description="Covid-19 cough detection ")
parser.add_argument("-f", type=str, help="audio filename")

args = parser.parse_args()

if args.f:
    res = predict(args.f)

    print(res)

    if 0.7 - res >= 1e-9:
        print("Di cach ly di ban oi!!!")
