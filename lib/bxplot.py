import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt


def get_data():
	"Generate some fake data."
	np.random.seed(937)
	data = np.random.lognormal(size=(37, 4), mean=1.5, sigma=1.75)
	labels = ["Set\nA",
			  "Set\nB",
			  "Set\nC",
			  "Set\nD"]
	return (data, labels)


def get_stats():
	"Compute the boxplot stats"
	(data, labels) = get_data()
	return mpl.cbook.boxplot_stats(data, labels=labels, bootstrap=10000)


def demo (axes, fontsize=10):
	"Demonstrate how to toggle the display of different elements"
	stats = get_stats()

	axes[0, 0].bxp(stats)
	axes[0, 0].set_title('Default', fontsize=fontsize)

	axes[0, 1].bxp(stats, showmeans=True)
	axes[0, 1].set_title('showmeans=True', fontsize=fontsize)

	axes[0, 2].bxp(stats, showmeans=True, meanline=True)
	axes[0, 2].set_title('showmeans=True,\nmeanline=True', fontsize=fontsize)

	axes[1, 0].bxp(stats, showbox=False, showcaps=False)
	axes[1, 0].set_title('Tufte Style',
						 fontsize=fontsize)

	axes[1, 1].bxp(stats, shownotches=True)
	axes[1, 1].set_title('notch=True', fontsize=fontsize)

	axes[1, 2].bxp(stats, showfliers=False)
	axes[1, 2].set_title('showfliers=False', fontsize=fontsize)

	for axis in axes.flatten():
	    axis.set_yscale('log')
	    axis.set_yticklabels([])
