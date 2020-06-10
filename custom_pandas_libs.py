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

def count_values_in_column(data: pd.DataFrame, feature: str):
    total = data.loc[:, feature].value_counts(dropna=False)
    percentage = round(data.loc[:, feature].value_counts(dropna=False, normalize=True)*100, 2)
    return pd.concat([total, percentage], axis=1, keys=['Total', 'Percentage'])

def duplicated_values_data(data):
    dup=[]
    columns=data.columns
    for i in data.columns:
        dup.append(sum(data[i].duplicated()))
    return pd.concat([pd.Series(columns),pd.Series(dup)],axis=1,keys=['Columns','Duplicate count'])

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

    cv = count_values_in_column(sample, "Name")
    print(cv)



