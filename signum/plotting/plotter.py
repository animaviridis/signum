import numpy as np
import matplotlib.pyplot as plt


class Plotter:
    def __init__(self, n_rows=1, n_cols=1, **kwargs):
        fig, axes = plt.subplots(n_rows, n_cols, **kwargs)
        if n_rows == 1 and n_cols == 1:
            axes = np.array([axes])
        axes = axes.reshape(n_rows, n_cols)

        self.fig = fig
        self.axes = axes

