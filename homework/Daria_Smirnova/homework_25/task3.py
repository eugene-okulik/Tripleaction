import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(6)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_language(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.qa-practice.com/elements/select/single_select")
    language_select = Select(driver.find_element(By.ID, "id_choose_language"))
    language_select.select_by_value("1")
    final = driver.find_element(By.ID, "submit-id-submit")
    final.click()

    wait.until(EC.presence_of_element_located((By.ID, "result")))
    entered_text = driver.find_element(By.XPATH, "//*[contains(text(), 'Python')]")
    assert "Python" in entered_text.text


def test_task2(driver):
    wait = WebDriverWait(driver, 15)
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    begin_button = driver.find_element(By.CSS_SELECTOR, "#start button")
    begin_button.click()

    hello = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[@id='finish']//h4"))
    )
    assert hello.text == "Hello World!"
#flake8
