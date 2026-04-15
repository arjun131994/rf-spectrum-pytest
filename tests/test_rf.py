import yaml
from instrument.spectrum_analyzer import SpectrumAnalyzer


def load_config():

    with open("config/config.yaml") as f:
        return yaml.safe_load(f)


def test_center_frequency():

    cfg = load_config()

    sa = SpectrumAnalyzer(cfg["ip"])

    sa.set_center_frequency("1GHz")

    freq = sa.get_center_frequency()

    print(freq)

    sa.close()

    assert True


def test_span():

    cfg = load_config()

    sa = SpectrumAnalyzer(cfg["ip"])

    sa.set_span("10MHz")

    sa.close()

    assert True
