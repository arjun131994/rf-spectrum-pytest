import pytest

@pytest.mark.skip(reason="Skip browser test in CI environment")
def test_google():

    from selenium import webdriver

    driver = webdriver.Chrome()

    driver.get("https://www.google.com")

    assert "Google" in driver.title

    driver.quit()
