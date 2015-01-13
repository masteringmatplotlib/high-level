"""
This code is adapted from the following matplotlib demo:
 * http://matplotlib.org/examples/style_sheets/plot_ggplot.html
"""
import numpy as np

import matplotlib.pyplot as plt


def scatter_demo(axes):
	"""Scatter plot

	Note: `plt.scatter` doesn't use default colors"""
	x, y = np.random.normal(size=(2, 200))
	axes.plot(x, y, 'o')


def sine_demo(axes):
	"Sinusoidal lines with colors from default color cycle."
	L = 2*np.pi
	x = np.linspace(0, L)
	ncolors = len(plt.rcParams['axes.color_cycle'])
	shift = np.linspace(0, L, ncolors, endpoint=False)
	for s in shift:
	    axes.plot(x, np.sin(x + s), '-')
	axes.margins(0)


def bar_graphs_demo(axes):
	"Bar graphs"
	x = np.arange(5)
	y1, y2 = np.random.randint(1, 25, size=(2, 5))
	width = 0.25
	axes.bar(x, y1, width)
	axes.bar(x+width, y2, width, color=plt.rcParams['axes.color_cycle'][2])
	axes.set_xticks(x+width)
	axes.set_xticklabels(['a', 'b', 'c', 'd', 'e'])


def circles_demo(axes):
	# circles with colors from default color cycle
	for i, color in enumerate(plt.rcParams['axes.color_cycle']):
	    xy = np.random.normal(size=2)
	    axes.add_patch(plt.Circle(xy, radius=0.3, color=color))
	axes.axis('equal')
	axes.margins(0)


def demo(axes):
	ax1, ax2, ax3, ax4 = axes.ravel()
	scatter_demo(ax1)
	sine_demo(ax2)
	bar_graphs_demo(ax3)
	circles_demo(ax4)
