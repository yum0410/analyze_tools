from matplotlib_venn import venn2
from matplotlib import pyplot
import os
import sys
import datetime
from make_histogram import is_file


def make_venn_plot(A=None, B=None, AB=None):
    ven = venn2(subsets=(A, B, AB))

    ven.get_patch_by_id('10').set_color('white')
    ven.get_patch_by_id('10').set_edgecolor('black')
    ven.get_patch_by_id('01').set_color('white')
    ven.get_patch_by_id('01').set_edgecolor('black')
    ven.get_patch_by_id('11').set_color('skyblue')
    ven.get_patch_by_id('11').set_edgecolor('black')
    
    # 背景色を変更する
    pyplot.gca().set_axis_on()
    pyplot.gca().set_facecolor('white')
    return pyplot

if __name__ == "__main__":
    sample_data = {"A": 3, "B": 2, "AB": 1}
    ven_plot = make_venn_plot(sample_data["A"], sample_data["B"], sample_data["AB"])
    save_path = "./sample_ven_plot/"

    # saving
    if save_path:
        if is_file(save_path, "png"):
            # make save path dir
            save_dir = os.path.join(*save_path.split("/")[:-1])
            os.makedirs(save_dir, exist_ok=True)
            ven_plot.savefig(os.path.join(save_path))
        else:
            # make save path dir
            os.makedirs(save_path, exist_ok=True)

            # file name as datetime_hist.png
            now = datetime.datetime.now()
            file_name = "{}_ven.png".format(now.strftime("%Y%m%d%H%M"))
            ven_plot.savefig(os.path.join(save_path, file_name))
