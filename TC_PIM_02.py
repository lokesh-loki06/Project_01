import time

from selenium import webdriver
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

        # click the user edit Symbol
        xpath_user = "(//i[@class='oxd-icon bi-pencil-fill'])[2]"
        login_tab = driver.find_element(By.XPATH, xpath_user)
        login_tab.click()

        # Clear the text field using xpath
        xpath_username_edit = "//input[@placeholder='First Name']"
        username = driver.find_element(By.XPATH, xpath_username_edit)
        time.sleep(6)
        username.clear()
        time.sleep(5)

        # Enter first name using xpath
        xpath_username_edit = "//input[@placeholder='First Name']"
        username = driver.find_element(By.XPATH, xpath_username_edit)
        username.send_keys("lokesh")

        # click the save button
        xpath_save_button = "(//button[@type='submit'][normalize-space()='Save'])[1]"
        save_tab = driver.find_element(By.XPATH, xpath_save_button)
        save_tab.click()
        time.sleep(3)

        # Validate the successfully saved popup
        if True:
            success = driver.find_element(By.XPATH, "//div[@id='oxd-toaster_1']")
            print(success.text)
            print("The user is Edited successfully")
        else:
            print("failed")

        driver.close()


go = test_Orange()
go.test()
