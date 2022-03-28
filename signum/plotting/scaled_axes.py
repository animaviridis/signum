import matplotlib.pyplot as plt

from signum.plotting.scaled_formatter import ScaledFormatter

_NOT_GIVEN_ = object()


class ScaledAxes:
    def __init__(self, ax: plt.Axes, x_unit='', y_unit='', x_label=None, y_label=None):
        if not isinstance(ax, plt.Axes):
            raise TypeError(f"Expected matplotlib.pyplot.Axes instance, got {type(ax)=}")

        self._ax = ax
        ax.xaxis.set_major_formatter(ScaledFormatter(x_unit))
        ax.yaxis.set_major_formatter(ScaledFormatter(y_unit))

        if x_label:
            self.set_xlabel(x_label)
        if y_label:
            self.xet_ylabel(y_label)

    def __getattr__(self, item):
        return getattr(self._ax, item)

    @property
    def ax(self):
        return self._ax

    def get_x_unit(self):
        return self.ax.xaxis.get_major_formatter().base_unit

    def set_x_unit(self, x_unit):
        self.ax.xaxis.get_major_formatter().base_unit = x_unit

    def get_y_unit(self):
        return self.ax.yaxis.get_major_formatter().base_unit

    def set_y_unit(self, y_unit):
        self.ax.yaxis.get_major_formatter().base_unit = y_unit

    def get_units(self):
        return self.get_x_unit(), self.get_y_unit()

    def set_units(self, x_unit, y_unit):
        self.set_x_unit(x_unit)
        self.set_y_unit(y_unit)
