from instrument.spectrum_analyzer import SpectrumAnalyzer

def test_frequency():

    sa = SpectrumAnalyzer()

    sa.set_frequency("1GHz")

    power = sa.read_power()

    assert power < 0
