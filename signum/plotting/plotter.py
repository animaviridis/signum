import numpy as np
import matplotlib.pyplot as plt
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from signum import SignalContainer


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

    def add_line(self, signal: 'SignalContainer', add_legend=True, **kwargs):
        if signal.description and 'label' not in kwargs:
            kwargs['label'] = signal.description

        lines = self._add_line(signal, **kwargs)

        if add_legend and 'label' in kwargs:
            self.add_legend()

        return lines

    def _add_line(self, signal, **kwargs):
        raise NotImplementedError


class SimplePlotter(Plotter):
    def __init__(self, **kwargs):
        super().__init__(n_rows=1, n_cols=1, **kwargs)

    @property
    def ax(self):
        return self.axes[0, 0]

    def _add_line(self, signal: 'SignalContainer', **kwargs):
        if np.iscomplexobj(signal):
            raise ValueError("Can't plot complex data on a SimplePlotter")

        line, = self.ax.plot(signal.x_axis, signal, **kwargs)

        return line,
