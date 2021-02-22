import numpy as np
import matplotlib.pyplot as plt


class Plotter:
    def __init__(self, n_rows=1, n_cols=1, **kwargs):
        fig_, axes_ = plt.subplots(n_rows, n_cols, **kwargs)
        if n_rows == 1 and n_cols == 1:
            axes_ = np.array([axes_])
        if axes_.ndim == 1:
            axes_ = axes_.reshape(-1, 1)

        self.fig = fig_
        self.axes = axes_

        self.plot_data = {}

