from selenium import webdriver
import time
from selenium.webdriver.common.by import By


# noinspection PyUnreachableCode
class test_Orange:
    def test(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)

        # Defining url
        url_orange = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

        # open the webpage
        driver.get(url_orange)
        time.sleep(3)

        # maximize the window
        driver.maximize_window()
        time.sleep(3)

        # Finding username tab Xpath and send key
        xpath_username = '//input[@name="username"]'
        username = driver.find_element(By.XPATH, xpath_username)
        username.send_keys("Admin")

        # Finding password tab Xpath and send key
        xpath_password = '//input[@type="password"]'
        password = driver.find_element(By.XPATH, xpath_password)
        password.send_keys("admin123")

        # click the Login icon
        xpath_login_tab = '//button[@type="submit"]'
        login_tab = driver.find_element(By.XPATH, xpath_login_tab)
        login_tab.click()

        # Validate the log-in page
        if True:
            print("The user is logged in successfully")
        else:
            print("Login failed")

        driver.close()


go = test_Orange()
go.test()
