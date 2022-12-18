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

        # click the PIM tab
        xpath_pim_tab = "//span[normalize-space()='PIM']"
        login_tab = driver.find_element(By.XPATH, xpath_pim_tab)
        login_tab.click()

        # click the user delete Symbol
        xpath_user_delete_symbol = "//div[@role='table']//div[1]//div[1]//div[9]//div[1]//button[1]//i[1]"
        login_tab = driver.find_element(By.XPATH, xpath_user_delete_symbol)
        login_tab.click()

        # click conform delete
        xpath_user_delete = "//button[normalize-space()='Yes, Delete']"
        login_tab = driver.find_element(By.XPATH, xpath_user_delete)
        login_tab.click()
        time.sleep(5)

        # Validate the successfully deleted
        if True:
            print("The user is deleted successfully")
        else:
            print("failed")

        driver.close()


go = test_Orange()
go.test()
