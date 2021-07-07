import numpy as np
from matplotlib import mlab


from signum.core.freq_domain_signal import BaseFreqDomainSignal as BaseFreqDomainSignal
from signum.core.time_domain_signal import BaseTimeDomainSignal as BaseTimeDomainSignal


class TimeDomainSignal(BaseTimeDomainSignal):
    @staticmethod
    def csd(x, y=None, **kwargs):
        """Cross spectral density"""

        y_in = y if y is not None else x

        # check that the operation is applicable to the inputs
        TimeDomainSignal.check_metadata(x, y_in, require_type=True)

        # calculate the spectrum
        spectrum, frequencies = mlab.csd(y_in, x, **kwargs, Fs=x.f_sampling)

        # cast type to FreqDomainSingal
        if y is None:
            description = f"{x.description}: power spectral density"
            meta = {**x.meta, 'original_description': x.description}
        else:
            description = f"{x.description} & {y.description}: cross spectral density"
            meta = {**x.meta, **y.meta, 'original_descriptions': [x.description, y.description]}

        spectrum = FreqDomainSignal(spectrum, f_resolution=frequencies[1] - frequencies[0], x_start=frequencies[0],
                                    description=description, meta=meta, unit=x.unit)

        return spectrum

    @staticmethod
    def psd(x, **kwargs):
        """Power spectral density"""

        return TimeDomainSignal.csd(x, **kwargs)


class FreqDomainSignal(BaseFreqDomainSignal):
    pass


if __name__ == '__main__':
    # time domain
    tdata1 = TimeDomainSignal(np.random.rand(12), f_sampling=40e6, description='Signal 1')
    tdata2 = TimeDomainSignal(np.arange(12).reshape(1, -1), f_sampling=1, unit='V', description='Signal 2')
    tdata3 = TimeDomainSignal(np.arange(12), f_sampling=40e6, description='Signal 3')

    tdata1.display()

    psd = TimeDomainSignal.psd(tdata1)
    psd.display()

    csd = TimeDomainSignal.csd(tdata1, tdata3)
    csd.display()

    # freq domain
    fdata1 = FreqDomainSignal(np.random.rand(12) + 1j * np.random.rand(12), f_resolution=10, unit='mV',
                              description="Frequency response")
    fdata2 = FreqDomainSignal(np.arange(12).reshape(1, -1), unit='V', description="H")

    fdata2.reshape(-1).display()
    fdata1.display()
    fdata1.display(complex_plot='bode', db_scale=True)
    fdata1.display(complex_plot='nyquist')
