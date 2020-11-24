import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import os
from collections import Counter, OrderedDict
import datetime
import pandas as pd
import numpy as np


FONT_PATH = "./ipaexg.ttf"
font_prop = FontProperties(fname=FONT_PATH)


def is_file(save_path, extension_type):
    """
    check save path is file path or dir path.

    Parameters
    ----------
    save_path : str
        target save path str.
    extension_type : str
        file extention type.

    Returns
    -------
    result : bool
        boolean of the save path is file path.
    """

    # remove dot(.) for current dir
    if "./" in save_path:
        save_path.replace("./", "")
    print(save_path)
    if "." + extension_type in save_path:
        return True
    return False


def save_png(save_path):
    if is_file(save_path, "png"):
        # make save path dir
        save_dir = os.path.join(*save_path.split("/")[:-1])
        os.makedirs(save_dir, exist_ok=True)
        plt.savefig(save_path)
    else:
        # make save path dir
        os.makedirs(save_path, exist_ok=True)

        # file name as datetime_hist.png
        now = datetime.datetime.now()
        file_name = "{}_hist.png".format(now.strftime("%Y%m%d%H%M"))
        plt.savefig(os.path.join(save_path, file_name))
    

def make_histogram(array, bar_title=None, save_path=None, sort_by_y=True, fill_x_nan=False, figsize=None):
    """
    make histogram

    Parameters
    ----------
    array : list
        input data. The histogram is computed over the flattened array.
    save_path : str
        the histogram　image file save path.
    sort_by_y : bool
        sorting flag.
    figsize : tuple
        figure_size. (x, y)
    Returns
    -------
    histogram_data : dict
        the value of the histogram
    """
    if type(array) is not list:
        raise ValueError("the method permit only list values.")
    # TODO support with pd.series

    # elif type(array) is type(pd.Series()):
    #     array.value_counts()

    # counting
    value_counts = Counter(array)

    # sorting
    if sort_by_y:
        # sorting by y(count)
        value_counts = OrderedDict(sorted(value_counts.items()))
    else:
        # sorting by x(value)
        value_counts = OrderedDict(value_counts.most_common())

    # fill_x_nan
    if fill_x_nan:
        if all([True if type(x) is int else False for x in array]):
            x_positions = range(min(array), max(array))
            for i in x_positions:
                if not value_counts.get(i):
                    value_counts[i] = 0
            value_counts = OrderedDict(sorted(value_counts.items(), key=lambda x: x[0]))

    # make plot
    plt.figure(figsize=figsize)
    x_positions = range(1, len(value_counts.keys())+1)
    print(x_positions, value_counts)
    plt.bar(x_positions, value_counts.values(), tick_label=value_counts.keys(), align="center")
    plt.xticks(x_positions, value_counts.keys(), fontproperties=font_prop, rotation=90)
    if bar_title:
        plt.title(bar_title, FontProperties=font_prop)

    # saving
    if save_path:
        save_png(save_path)
    return value_counts


def make_stack_bar_plot(values, bar_title=None, save_path=None):
    plt.figure()
    fig, ax = plt.subplots()
    for i in range(len(dataset)):
        ax.bar(dataset.columns, dataset.iloc[i], bottom=dataset.iloc[:i].sum())
    plt.legend(dataset.index, prop=font_prop)
    if bar_title:
        plt.title(bar_title, FontProperties=font_prop)
    # saving
    if save_path:
        save_png(save_path)


def make_pareto_chart(bar_value_counts, line_array, x_labels=None, bar_title=None, save_path=None):
    plt.figure()
    fig, ax1 = plt.subplots()
    ax1.bar(range(len(bar_value_counts)), bar_value_counts.values)
    ax1.set_xticks(range(len(bar_value_counts)))
    if x_labels:
        ax1.set_xticklabels(x_labels, fontproperties=font_prop)
    else:
        ax1.set_xticklabels(bar_value_counts.keys())
    ax1.set_xlabel("label")
    ax1.set_ylabel("counts")

    ax2 = ax1.twinx()
    ax2.plot(range(len(bar_value_counts)), line_array, c="k", marker="o")
    ax2.set_ylim([0, 100])
    ax2.grid(True, which='both', axis='y')
    if bar_title:
        plt.title(bar_title, FontProperties=font_prop)
    # saving
    if save_path:
        save_png(save_path)


if __name__ == "__main__":
    hoge = ["A", "A", "A", "B", "A", "B", "C", "C", "D"]
    print(make_histogram(hoge, "hoge_ヒストグラム", "./hoge/hoge.png"))
    huga = [4, 1, 5, 4, 4, 10]
    print(make_histogram(huga, "huga_ヒストグラム", "./huga/huga.png", sort_by_y=False, fill_x_nan=True))
    dataset = pd.DataFrame([[100, 200, 300], [300, 400, 500]],
                        columns=['A', 'B', 'C'], 
                        index=['正解', '不正解'])
    make_stack_bar_plot(dataset, "stack_bar_plot", "./piyo/piyo.png")
    dataset = pd.DataFrame({"A": [42, 33, 25, 50, 15, 35]})
    dataset = dataset.sort_values(by="A", ascending=False)
    dataset["sum"] = np.cumsum(dataset["A"])
    dataset["percent"] = [(x / max(dataset["sum"])) * 100 for x in dataset["sum"]]
    make_pareto_chart(dataset["A"], dataset["percent"], ["あ", "い", "ウ", "絵", "お", "蚊"], "pareto_chart", "./pareto_chart/p2.png")
    print(dataset)
