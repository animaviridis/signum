import numpy as np
import matplotlib.pyplot as plt
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from signum import SignalContainer

from signum.plotting.plotter import Plotter


class IQPlotter(Plotter):
    def __init__(self, figsize=(8, 6), **kwargs):
        super().__init__(n_rows=2, n_cols=1, figsize=figsize, **kwargs)

        self.i_ax.set_ylabel("Real")
        self.q_ax.set_ylabel("Imag")

    @property
    def i_ax(self) -> plt.Axes:
        return self.axes[0, 0]

    @property
    def q_ax(self) -> plt.Axes:
        return self.axes[1, 0]

    def _add_line(self, signal: 'SignalContainer', **kwargs):
        i_line, = self.i_ax.plot(signal.x_axis, signal.real.T, **kwargs)
        q_line, = self.q_ax.plot(signal.x_axis, signal.imag.T, **kwargs)

        return i_line, q_line


if __name__ == '__main__':
    from signum import TimeDomainSignal

    s1 = TimeDomainSignal(np.random.rand(10) + 1j * np.random.rand(10), f_sampling=2, description='Random data')

    x = np.arange(-3, 3, 0.1)
    s2 = TimeDomainSignal(x**2/2 - 2, description="x^2", x_axis=x)

    plot = IQPlotter(title='IQ plot')
    plot.add_line(s1, marker='d')
    plot.add_line(s2, color='crimson', label='Square func')
    plot.show_all()
