import pandas as pd
import numpy as np
from itertools import chain

def check_to_csv(df):

    drop_index = False
    # check numerical index
    if df.index.dtype.type is np.int64:
        if all(range(min(df.index), max(df.index)+1) == df.index.values):
            drop_index = True

    # check exceed upper limit(32767 words) word counts.
    LIMIT_WORD_COUNT = 32767
    categorical_feats= df.dtypes[df.dtypes == "object"].index
    if any(chain.from_iterable(df[categorical_feats].applymap(lambda x: len(x) >= LIMIT_WORD_COUNT).values)):
        raise Exception("over limit word count!")
    return {"drop_index": drop_index}

if __name__ == "__main__":
    sample = pd.DataFrame({
        "ID": [1, 2, 3],
        "Name": ["hoge", "huga", "piyo"],
        "score": [60, 40, 100],
        "height": [160, 145, 175],
        "sex": [1, 0, 0],
        "description": ["", "", "piyo"*8191]
    })
    result = check_to_csv(sample)
    sample.to_csv("sample.csv", index=result["drop_index"])