from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
from time import sleep

def get_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--use-fake-ui-for-media-stream")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def save_cookies(driver, filename):
    driver.get('https://accounts.snapchat.com/v2/welcome')
    sleep(3)
    with open(filename, 'wb') as f:
        pickle.dump(driver.get_cookies(), f)
    print("Cookies saved successfully")
    driver.get("https://web.snapchat.com/")

def add_cookies(driver, filename):
    driver.get('https://accounts.snapchat.com/v2/welcome')
    sleep(3)
    try:
        cookies = pickle.load(open(filename, 'rb'))
        for cookie in cookies:
            driver.add_cookie(cookie)
        print("Cookies added successfully")
        driver.get('https://web.snapchat.com/')
        return True
    except Exception as e:
        print("Failed to add cookies:", e)
        return False

def login(driver, username, password):
    driver.refresh()
    sleep(3)
    try:
        login_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='ai_input']")))
        login_input.send_keys(username)

        login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Log in']")))
        login_button.click()

        password_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='password']")))
        password_input.send_keys(password)

        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Next']"))).click()

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Not now']"))).click()
        print("Logged in successfully")
        return True
    except Exception as e:
        print("Failed to login:", e)
        return False

def send_snap(driver, usernames):
    try:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.FBYjn.gK0xL.W5dIq'))).click()
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//button[@class="FBYjn gK0xL A7Cr_ m3ODJ"]'))).click()
        sleep(3)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Send To"]'))).click()
        for username in usernames:
            input_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '(//input[@class="dmsdi"])[2]')))
            input_element.send_keys(username)
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="hSQnC"]'))).click()
            input_element.send_keys(Keys.BACKSPACE)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="TYX6O eKaL7 Bnaur"]'))).click()
        print("Snap sent successfully to: ", ', '.join(usernames))
    except Exception as e:
        print("Failed to send snap:", e)

def main():
    driver = get_driver()
    try:
        driver.get("https://www.snapchat.com")
        if add_cookies(driver, "cookies.pkl"):
            print("Cookies added successfully.")
        else:
            username = input("Enter your Snapchat username: ")
            password = input("Enter your Snapchat password: ")
            if login(driver, username, password):
                save_cookies(driver, "cookies.pkl")
        usernames = ["user1", "user2", "user3"]  # Add usernames here
        send_snap(driver, usernames)
    except Exception as e:
        print("An error occurred:", e)
    finally:
        input("Press Enter to close the browser...")
        driver.quit()

if __name__ == "__main__":
    main()
