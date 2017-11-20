"""
read .mat file (MATLAB) and draw histogram
"""

import math
import os
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
import scipy.io as scio


# set style of seaborn 
sns.set(color_codes=True, font_scale=1.4)
sns.set_style("whitegrid", {'axes.edgecolor': '0.0',
                            'grid.color': '.8', 'legend.frameon': True})


def main():
    """
    main function
    """
    # define path for saving figures
    fig_path = "./fig/"
    # if the directory not exists, create it
    if not os.path.isdir(fig_path):
        os.mkdir(fig_path)

    data_file = "data.mat"
    # load .mat file
    data = scio.loadmat(data_file)
    # data from .mat file is converted into dictionary
    input_data = data["rand_input"]

    # set charateristic of histogram
    width = 0.5
    legend_size = 20

    # compute bins according to pre-defined bin width
    max_input = input_data.max()
    min_input = input_data.min()
    fig_bins = np.arange(math.floor(min_input / width) *
                         width, math.ceil(max_input / width + 1) * width, width)

    # save figures
    plt.figure()
    sns.distplot(input_data, bins=fig_bins, kde=False,
                 norm_hist=True, label="rand_input", color="blue")

    plt.legend(loc=0, prop={"size": legend_size})
    plt.xlabel("input_data")
    plt.ylabel("probability")
    # plt.show()
    plt.savefig(os.path.join(fig_path, "fig_without_kde.png"))

    # save figures
    plt.figure()
    sns.distplot(input_data, bins=fig_bins, kde=True,
                 norm_hist=False, label="rand_input", color="blue")

    plt.legend(loc=0, prop={"size": legend_size})
    plt.xlabel("input_data")
    plt.ylabel("probability")
    # plt.show()
    plt.savefig(os.path.join(fig_path, "fig_with_kde.png"))


if __name__ == "__main__":
    main()
