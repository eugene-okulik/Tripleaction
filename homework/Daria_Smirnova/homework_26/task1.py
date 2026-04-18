import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(6)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_added_product(driver):
    driver.get("http://testshop.qa-practice.com/")
    product = driver.find_element(By.CSS_SELECTOR, 'a[href="/shop/customizable-desk-9"] img')
    ActionChains(driver).key_down(Keys.CONTROL).click(product).key_up(Keys.CONTROL).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    add_button = driver.find_element(By.ID, "add_to_cart")
    add_button.click()

    wait = WebDriverWait(driver, 8)
    Alert(driver)
    continue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-secondary")))
    continue_button.click()

    wait = WebDriverWait(driver, 8)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".my_cart_quantity"), "1"))
    driver.close()

    driver.switch_to.window(tabs[0])
    wait = WebDriverWait(driver, 10)

    cart = driver.find_element(By.CSS_SELECTOR, 'a[href="/shop/cart"]')
    cart.click()
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".my_cart_quantity"), "1"))
    added_product = driver.find_element(By.CSS_SELECTOR, '.o_cart_product[data-product-id="12"]')
    assert "Customizable Desk" in added_product.text


def test_pop_up(driver):
    driver.get("http://testshop.qa-practice.com/")
    actions = ActionChains(driver)
    product = driver.find_element(By.CSS_SELECTOR, 'a[href="/shop/customizable-desk-9"] img')
    card = driver.find_element(By.CSS_SELECTOR, "a.btn.btn-primary.a-submit")
    actions.move_to_element(product)
    actions.move_to_element(card)
    actions.click(card)
    actions.perform()

    wait = WebDriverWait(driver, 8)
    Alert(driver)
    added_product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.product_id[value="12"]')))
    assert added_product.get_attribute("value") == "12"
