from matplotlib import pyplot as plt
import numpy as np


def get_ranking_num(list):
    for i, x in enumerate(list):
        if x > 0:
            return i + 1
    return np.inf


if __name__ == "__main__":
    data = {
        "no1": [0, 0, 0, 0, 0],
        "no2": [0, 0, 0, 1, 0],
        "no3": [0, 0, 0, 0, 0],
        "no4": [0, 1, 0, 0, 0],
        "no5": [0, 0, 0, 0, 1],
        "no6": [1, 0, 0, 0, 0],
        "no7": [0, 0, 1, 0, 0],
        "no8": [1, 0, 0, 0, 0],
        "no9": [0, 0, 0, 0, 1],
        "no10": [0, 0, 0, 0, 0]
    }
    ranking_num = {k: get_ranking_num(v) for k, v in data.items()}
    sort_index_map = {i: x[0] for i, x in enumerate(sorted(ranking_num.items(), key=lambda x: x[1]))}

    # sorted_by_ranking
    sorted_by_ranking_data = [0] * len(data)
    for k, v in sort_index_map.items():
        sorted_by_ranking_data[k] = data[v]

    plt.matshow(sorted_by_ranking_data)
    plt.savefig("./sample_ranking_plot.png")
