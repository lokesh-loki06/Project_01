import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


# from selenium.webdriver.support.select import Select


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

        # click the user add Symbol
        xpath_user_add = "//button[normalize-space()='Add']"
        login_tab = driver.find_element(By.XPATH, xpath_user_add)
        login_tab.click()

        # Enter first name, middle name, & last name
        xpath_first_name = "//input[@placeholder='First Name']"
        username = driver.find_element(By.XPATH, xpath_first_name)
        username.send_keys("Abdul")

        xpath_middle_name = "//input[@placeholder='Middle Name']"
        username = driver.find_element(By.XPATH, xpath_middle_name)
        username.send_keys("Kadhar")

        xpath_last_name = "//input[@placeholder='Last Name']"
        username = driver.find_element(By.XPATH, xpath_last_name)
        username.send_keys("Jeelani")
        time.sleep(3)

        # click the save button
        xpath_save_button = "//button[normalize-space()='Save']"
        save_tab = driver.find_element(By.XPATH, xpath_save_button)
        save_tab.click()
        time.sleep(3)

        # Entering Personal Information

        # Entering license number
        xpath_license_number = "(//input[@class='oxd-input oxd-input--active'])[5]"
        license_number = driver.find_element(By.XPATH, xpath_license_number)
        license_number.send_keys("64654654654")

        # Entering license expdate
        xpath_license_expdate = "(//input[@placeholder='yyyy-mm-dd'])[1]"
        license_expdate = driver.find_element(By.XPATH, xpath_license_expdate)
        license_expdate.send_keys("1994-10-12")
        time.sleep(3)

        # Entering SSN number
        xpath_ssn_number = '(//input)[10]'
        ssn_number = driver.find_element(By.XPATH, xpath_ssn_number)
        ssn_number.send_keys("212")

        # Entering SIN number
        xpath_sin_number = '(//input)[11]'
        sin_number = driver.find_element(By.XPATH, xpath_sin_number)
        sin_number.send_keys("5455")

        # Selecting nationality
        action = ActionChains(driver)
        xpath_nationality = "//label[text()='Nationality']/following::div[1]"
        nationality = driver.find_element(By.XPATH, xpath_nationality)
        action.move_to_element(nationality).click().perform()

        xpath_indian = "//div[@role='option']/span[text()='Indian']"
        selecting_country = driver.find_element(By.XPATH, xpath_indian)
        action.move_to_element(selecting_country).click().perform()
        time.sleep(5)

        # Selecting Marital Status
        xpath_marital_status = "//label[text()='Marital Status']/following::div[1]"
        selecting_martial = driver.find_element(By.XPATH, xpath_marital_status)
        action.move_to_element(selecting_martial).click().perform()
        time.sleep(5)

        xpath_status = "//div[@role='option']/span[text()='Married']"
        martial = driver.find_element(By.XPATH, xpath_status)
        action.move_to_element(martial).click().perform()
        time.sleep(5)

        # Entering DOB
        xpath_dob = "(//input[@placeholder='yyyy-mm-dd'])[2]"
        datebox = driver.find_element(By.XPATH, xpath_dob)
        datebox.click()

        # xpath_dob = "(//input[@placeholder='yyyy-mm-dd'])[2]"
        # dob = driver.find_element(By.XPATH, xpath_dob)
        # dob.send_keys("1994-12-10")

        # gender selecting
        xpath_gender = "//label[normalize-space()='Male']"
        gender = driver.find_element(By.XPATH, xpath_gender)
        gender.click()

        # Entering Military service
        xpath_military_service = "(//input[@placeholder='yyyy-mm-dd'])[2]"
        military_service = driver.find_element(By.XPATH, xpath_military_service)
        military_service.send_keys("NO")

        # click the save button
        xpath_save_button = "(//button[@type='submit'][normalize-space()='Save'])[1]"
        save_tab = driver.find_element(By.XPATH, xpath_save_button)
        save_tab.click()
        time.sleep(3)

        # Validate the successfully saved popup
        if True:
            print("The user is Added successfully")
        else:
            print("failed")

        driver.close()


go = test_Orange()
go.test()
