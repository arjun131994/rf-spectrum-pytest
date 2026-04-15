from selenium import webdriver


def test_google():

    driver = webdriver.Chrome()

    driver.get("https://www.google.com")

    print(driver.title)

    driver.quit()

    assert True
