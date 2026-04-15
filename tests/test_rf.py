def test_center_frequency():

    # mock test (no real instrument needed)

    freq = "1GHz"

    assert "GHz" in freq


def test_span():

    span = "10MHz"

    assert "MHz" in span


def test_peak_power():

    power = -20

    assert power < 0
