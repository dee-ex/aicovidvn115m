import pickle
import numpy as np
import pandas as pd
import lightgbm as lgbm
from sklearn.model_selection import KFold
from imblearn.over_sampling import SVMSMOTE

def prepare():
    mfcc = pd.read_csv("../data/train_features/minmax_mfcc_features.csv")
    chroma = pd.read_csv("../data/train_features/minmax_chroma_features.csv")
    mel = pd.read_csv("../data/train_features/minmax_mel_features.csv")
    zcr = pd.read_csv("../data/train_features/minmax_zcr_features.csv")

    train_df = pd.concat([zcr.iloc[:, :-1],
                        mfcc.iloc[:, :-1],
                        chroma.iloc[:, :-1], mel], axis=1)

    X, y = train_df.iloc[:, :-1].values, train_df.iloc[:, -1].values

    print(X.shape, y.shape)

    smote = SVMSMOTE(sampling_strategy=1, random_state=42)

    return X, y, smote

def train():
    X, y, smote = prepare()

    params = {"objective": "binary",
              "boosting_type": "gbdt",
              "metric" : "auc",
              "learning_rate": 0.03,
              "subsample": 0.68,
              "tree_learner": "serial",
              "colsample_bytree": 0.28,
              "early_stopping_rounds": 100,
              "subsample_freq": 1,
              "reg_lambda": 2,
              "reg_alpha": 1,
              "num_leaves": 500,
              "random_state": 42,}

    seeds = range(10)
    fold_seed = 42
    n_splits = 10

    for seed in seeds:

        print("---seed: ", seed)

        kfolds = KFold(n_splits=n_splits, random_state=fold_seed, shuffle=True)

        for f, (trn_idx, val_idx) in enumerate(kfolds.split(X=X, y=y)):

            kf_x_train, kf_y_train = X[trn_idx], y[trn_idx]
            kf_x_train, kf_y_train = smote.fit_resample(kf_x_train, kf_y_train)
            kf_x_valid, kf_y_valid = X[val_idx], y[val_idx]
            
            print(kf_x_train.shape, kf_y_train.shape)
            
            dtrain = lgbm.Dataset(kf_x_train, kf_y_train)
            dvalid = lgbm.Dataset(kf_x_valid, kf_y_valid)
            
            params["random_state"] = seed
            params["num_leaves"] = 500 + seed * 25

            model = lgbm.train(params, 
                              dtrain, 
                              num_boost_round=10000,
                              early_stopping_rounds=params["early_stopping_rounds"],
                              valid_sets=(dtrain, dvalid), 
                              valid_names=("train", "valid"),
                              verbose_eval = 100)

            f = open(f"../weights/model_{seed + 1}_{f + 1}.pkl", "wb")
            pickle.dump(model, f)
            f.close()

            print('=' * 80)

if __name__ == "__main__":
    train()
