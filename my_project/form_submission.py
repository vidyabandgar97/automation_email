from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def submit_google_form():

    # Path to your chromedriver executable
    chrome_driver_path = "D:\\dya\\chromedriver.exe"

    # Set up the webdriver service
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)


    # Open the Google Form
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/viewform')

    time.sleep(2)  # Wait for the page to load

    # Fill out the form (example fields, adjust according to the form structure)
    name_field = driver.find_element(By.XPATH, '//input[@type="text"]')
    name_field.send_keys("Vidya Bandgar")

    time.sleep(2)
            
    number_field = driver.find_element(By.XPATH, '(//input[@class="whsOnd zHQkBf"])[2]')
    number_field.send_keys("8963920432")

    time.sleep(2)

    email_field = driver.find_element(By.XPATH, '(//input[@class="whsOnd zHQkBf"])[3]')
    email_field.send_keys("vidyabandgar97.email@example.com")

    time.sleep(2)

    Address_field = driver.find_element(By.XPATH, '(//*[@class="KHxj8b tL9Q4c"])')
    Address_field.send_keys("Mumbai")

    time.sleep(2)

    pincode_field = driver.find_element(By.XPATH, '(//input[@class="whsOnd zHQkBf"])[4]')
    pincode_field.send_keys("401208")

    time.sleep(2)

    date_field = driver.find_element(By.XPATH, '(//input[@class="whsOnd zHQkBf"])[5]')
    date_field.send_keys("04/12/2024")

    time.sleep(2)

    gender_field = driver.find_element(By.XPATH, '(//input[@class="whsOnd zHQkBf"])[6]')
    gender_field.send_keys("Female")

    time.sleep(2)

    code_field = driver.find_element(By.XPATH, '(//span[@class="M7eMe"])[8]')
    text = code_field.text
    code = text.split(": ")[1]

    # Wait for the element to be clickable and interactable
    code_field1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '(//input[@class="whsOnd zHQkBf"])[7]'))
    )

    # Check if the element is visible and enabled
    if code_field1.is_displayed() and code_field1.is_enabled():
        code_field1.send_keys(code)

    
    time.sleep(2)
    submit_button = driver.find_element(By.XPATH, '//span[contains(text(),"Submit")]')
    submit_button.click()
    
    time.sleep(2)
    
    # Capture a screenshot
    screenshot_path = 'D:\\dya\\itershala\\automategform\\my_project\\email_sender\\management\\commands\\confirmation_page.png'
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved at: {screenshot_path}")
    
    return screenshot_path


if __name__ == "__main__":
    submit_google_form()
