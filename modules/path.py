import os
import pandas as pd

# ==============================================================================

def build_path():
    train_meta_df = pd.read_csv("../data/train_metadata.csv")
    train_meta_df = train_meta_df.loc[train_meta_df["audio_noise_note"].isnull()]

    train_df = pd.DataFrame()
    train_df["path"] = train_meta_df["uuid"].apply(lambda uuid: f"../data/train/{uuid}.wav")
    train_df["label"] = train_meta_df["assessment_result"]

    # ==============================================================================

    extra_dir = os.listdir("../data/extra")

    extra_df = pd.DataFrame()
    extra_df["path"] = ["extra/" + fname for fname in extra_dir]
    extra_df["label"] = 1

    # ==============================================================================

    train_df = pd.concat([train_df, extra_df], axis=0)

    train_df.to_csv("../data/train.csv", index=False)

    # ==============================================================================

    private_df = pd.read_csv("../data/private_metadata.csv")

    private_df["assessment_result"] = private_df["uuid"].apply(lambda uuid: f"../data/private/{uuid}.wav")
    private_df.columns = ["uuid", "path"]

    private_df.to_csv("../data/private.csv", index=False)

if __name__ == "__main__":
    build_path()
