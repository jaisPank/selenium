from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service_obj = Service("/home/shtlp_0031/my_learning/python/selenium/chromedriver")
driver = webdriver.Chrome(service=service_obj)
wait = WebDriverWait(driver, 10)  # Maximum wait time of 10 seconds

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

try:
    # Wait for the username input field to become visible
    username_input = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
    
    # Locate the password input field and login button
    password_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    login_button = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")))
    
    # Entering values and clicking the login button
    username_input.send_keys("Admin")
    password_input.send_keys("admin123")
    login_button.click()
    
    title1 = driver.title
    exp_title = "OrangeHRM"
    if title1 == exp_title:
        print("Login Successful")
    else:
        print("Login Failed")
except Exception as e:
    print("An error occurred:", e)

driver.quit()
