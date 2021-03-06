import numpy as np
import pandas as pd
import scipy
from collections import Counter
import seaborn as sns
import matplotlib.pyplot as plt


def get_basic_statics(x):
    """
    get basic statics infomation of target values.


    Parameters
    ----------
    x : list
        target values. supproted type is str, int, float, DataFrame.

    Returns
    -------
    result : dict
        basic statics infomation.
    """
    np.warnings.filterwarnings('ignore')

    # check contain str values
    if str not in set(map(type, x)):
        c = Counter(x)
        result = {
            "max": max(x),
            "min": min(x),
            "average": np.nanmean(x),
            "median": np.nanmedian(x),
            "variance": np.var(x),
            "std": np.std(x),
            "skew": scipy.stats.skew(x),
            "kurtosis": scipy.stats.kurtosis(x),
            "missing rario": pd.Series(x).isna().sum() / len(x),
            "unique counts": len(c.keys()),
            "most label": c.most_common()[0][0],
            "most label counts": c.most_common()[0][1]
        }
    else:
        c = Counter(x)
        result = {
            "missing rario": pd.Series(x).isna().sum() / len(x),
            "unique counts": len(c.keys()),
            "most label": c.most_common()[0][0],
            "most label counts": c.most_common()[0][1]
        }
    return result


def get_crosstab(x, y):
    ct = pd.crosstab(x, y)
    table = np.array(ct).astype(np.float32)
    n = table.sum()
    colsum = table.sum(axis=0)
    rowsum = table.sum(axis=1)
    expect = np.outer(rowsum, colsum) / n
    chisq = np.sum((table - expect) ** 2 / expect)
    return ct, np.sqrt(chisq / (n * (np.min(table.shape) - 1)))


if __name__ == "__main__":
    hoge = ["A", "A", "A", "B", "A", "B", "C", "C", "D"]
    huga = [1, 0.5, 3, 4, np.nan]
    s1 = pd.Series(get_basic_statics(hoge), name="hoge")
    s2 = pd.Series(get_basic_statics(huga), name="huga")
    pd.DataFrame([s1, s2]).T.to_csv("./basic_statics_sample.csv")

    # get basic statics from DataFrame
    sample = pd.DataFrame({
        "ID": [1, 2, 3],
        "Name": ["hoge", "huga", "piyo"],
        "score": [60, 40, 100],
        "height": [160, 145, 175],
        "sex": [1, 0, 0]
    })
    report_path = "./basic_statics_from_DF.csv"
    sample.describe(include="all").to_csv(report_path, encoding="utf-8-sig")

    # classification featurs
    numerical_feats = sample.dtypes[sample.dtypes != "object"].index
    categorical_feats= sample.dtypes[sample.dtypes == "object"].index

    # plot 回帰直線
    sns.regplot(x=numerical_feats[0], y=numerical_feats[1], data=sample)
    plt.savefig("./seaborntest.png")

    # ラベル間の相関係数を測定
    ct, score = get_crosstab(sample["Name"], sample["sex"])
    print(score)
    print(ct)
