import numpy as np
import matplotlib.pyplot as plt

from signum import SignalContainer, FreqDomainSignal
from signum.plotting.plotter import Plotter


class PolarPlotter(Plotter):
    def __init__(self, figsize=(6, 6), db_scale=False, **kwargs):
        super().__init__(n_rows=1, n_cols=1, figsize=figsize, subplot_kw={'projection': 'polar'}, **kwargs)

        self._db_scale = db_scale

        self.ax.grid(color='lightgrey')

    @property
    def ax(self) -> plt.Axes:
        return self.axes[0, 0]

    def _add_line(self, signal: SignalContainer, set_equal_limits=True, **kwargs):
        mag = signal.magnitude_db if self._db_scale else signal.magnitude
        phase = signal.get_phase(rad=True)

        line, = self.ax.plot(phase.T, mag.T, **kwargs)

        return line,


if __name__ == '__main__':
    s1 = FreqDomainSignal(np.random.rand(10) + 1j * np.random.rand(10), f_resolution=2, description='Random data')

    x = np.arange(20, step=0.1)
    s2 = FreqDomainSignal(x/20 * (np.cos(x) + 1j * np.sin(x)), x_axis=x)

    plot = PolarPlotter(title='Polar plot')
    plot.add_line(s1, marker='d', linestyle=':')
    plot.add_line(s2, color='crimson', label='Spiral')
    plot.show_all()
