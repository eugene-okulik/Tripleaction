from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)
driver.get("https://www.qa-practice.com/elements/input/simple")
input_text = "tester"

text_string = wait.until(EC.element_to_be_clickable((By.ID, "id_text_string")))
text_string.send_keys(input_text)
text_string.submit()
entered_text = driver.find_element(By.XPATH, "//*[contains(text(), 'tester')]")
print(entered_text.text)
