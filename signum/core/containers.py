import numpy as np
from matplotlib import mlab


from signum.core.freq_domain_signal import BaseFreqDomainSignal as BaseFreqDomainSignal
from signum.core.time_domain_signal import BaseTimeDomainSignal as BaseTimeDomainSignal


class TimeDomainSignal(BaseTimeDomainSignal):
    def csd(self, other=None, **kwargs):
        """Cross spectral density"""

        if other is None:
            description = f"{self.description}: power spectral density"
            meta = {**self.meta, 'original_description': self.description}
            other = self

        else:
            # check that the operation is applicable to the inputs
            self.check_metadata(self, other, require_type=True)

            description = f"{self.description} & {other.description}: cross spectral density"
            meta = {**self.meta, **other.meta, 'original_descriptions': [self.description, other.description]}

        # calculate the spectrum
        spectrum, frequencies = mlab.csd(other, self, **kwargs, Fs=self.f_sampling)

        spectrum = FreqDomainSignal(spectrum, f_resolution=frequencies[1] - frequencies[0], x_start=frequencies[0],
                                    description=description, meta=meta, unit=self.unit)

        return spectrum

    def psd(self, **kwargs):
        """Power spectral density"""

        return self.csd(other=None, **kwargs)


class FreqDomainSignal(BaseFreqDomainSignal):
    pass


if __name__ == '__main__':
    # time domain
    tdata1 = TimeDomainSignal(np.random.rand(12), f_sampling=40e6, description='Signal 1')
    tdata2 = TimeDomainSignal(np.arange(12).reshape(1, -1), f_sampling=1, unit='V', description='Signal 2')
    tdata3 = TimeDomainSignal(np.arange(12), f_sampling=40e6, description='Signal 3')

    tdata1.display()

    psd = tdata1.psd()
    psd.display()

    csd = tdata1.csd(tdata3)
    csd.display()

    # freq domain
    fdata1 = FreqDomainSignal(np.random.rand(12) + 1j * np.random.rand(12), f_resolution=10, unit='mV',
                              description="Frequency response")
    fdata2 = FreqDomainSignal(np.arange(12).reshape(1, -1), unit='V', description="H")

    fdata2.reshape(-1).display()
    fdata1.display()
    fdata1.display(complex_plot='bode', db_scale=True)
    fdata1.display(complex_plot='nyquist')
