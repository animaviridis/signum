import numpy as np
import matplotlib.pyplot as plt


class Plotter:
    def __init__(self, n_rows=1, n_cols=1, title=None, **kwargs):
        fig, axes = plt.subplots(n_rows, n_cols, **kwargs)
        if n_rows == 1 and n_cols == 1:
            axes = np.array([axes])
        axes = axes.reshape(n_rows, n_cols)

        self.fig = fig
        self.axes = axes

        if title:
            fig.suptitle(title)

        for ax in axes.flatten():
            ax.grid(color='lightgrey')

    def add_legend(self, **kwargs):
        """Add legend to each of the main grid axes."""

        for ax in self.axes.flatten():
            ax.legend(fancybox=True, framealpha=0.5, **kwargs)

    def show_fig(self, **kwargs):
        self.fig.show(**kwargs)

    @staticmethod
    def show_all(**kwargs):
        plt.show(**kwargs)
