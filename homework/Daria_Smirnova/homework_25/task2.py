from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=500,1080")
driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")

wait = WebDriverWait(driver, 5)
name = driver.find_element(By.CSS_SELECTOR, "#firstName")
name.send_keys("Pedro")

last_name = driver.find_element(By.XPATH, '//*[@id="lastName"]')
last_name.send_keys("Sanchez")

input_email = "pedro@gmail.com"
email = driver.find_element(By.ID, "userEmail")
email.send_keys(input_email)

gender = wait.until(EC.element_to_be_clickable((By.ID, "gender-radio-1")))
gender.click()

input_mobile = "1234567890"
mobile = driver.find_element(By.ID, "userNumber")
mobile.send_keys(input_mobile)

birth_date = wait.until(EC.element_to_be_clickable((By.ID, "dateOfBirthInput")))
birth_date.click()
month_select = Select(
    driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")
)
month_select.select_by_visible_text("January")

year_select = Select(
    driver.find_element(By.CLASS_NAME, "react-datepicker__year-select")
)
year_select.select_by_value("1995")

day = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//div[@aria-label='Choose Sunday, January 8th, 1995']")
    )
)
day.click()

subjects = wait.until(EC.element_to_be_clickable((By.ID, "subjectsInput")))
subjects.click()
subjects.clear()
subjects.send_keys("Maths")

math = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "//div[contains(@class,'subjects-auto-complete__option') and text()='Maths']",
        )
    )
)
math.click()

hobbies = wait.until(EC.element_to_be_clickable((By.ID, "hobbies-checkbox-1")))
hobbies.click()

current_address = wait.until(EC.element_to_be_clickable((By.ID, "currentAddress")))
current_address.send_keys("Barcelona, Camp Nou")

state = wait.until(EC.element_to_be_clickable((By.ID, "react-select-3-input")))
state.click()
state.send_keys("NCR")

ncr = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'NCR')]"))
)
ncr.click()

city = wait.until(EC.element_to_be_clickable((By.ID, "react-select-4-input")))
city.click()
city.send_keys("Delhi")

delhi = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Delhi')]"))
)
delhi.click()

submit_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
submit_button.click()

new_element = wait.until(
    EC.presence_of_element_located((By.ID, "example-modal-sizes-title-lg"))
)
table = driver.find_element(
    By.CSS_SELECTOR, "table.table-dark.table-striped.table-bordered.table-hover"
)
print(table.text)
