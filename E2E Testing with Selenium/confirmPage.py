#self.driver.find_element(By.ID, 'country').send_keys('po')
#By.XPATH, '//div[@class="suggestions"]//a[text()="Portugal"]'
#self.driver.find_element(By.XPATH, '//label[@for="checkbox2"]').click()
#self.driver.find_element(By.XPATH, '//form/input[@value="Purchase"]').click()
#self.driver.find_element(By.CLASS_NAME, "alert-success").text
from selenium.webdriver.common.by import By


class Confirm():
    def __init__(self, driver):
        self.driver = driver

    find_country = (By.ID, 'country')
    confirm_cb = (By.XPATH, '//label[@for="checkbox2"]')
    btn_purchase = (By.XPATH, '//form/input[@value="Purchase"]')
    txt_success = (By.CLASS_NAME, 'alert-success')



    def dropdown_find_country(self):
        return self.driver.find_element(*Confirm.find_country)

    def click_confirm(self):
        return self.driver.find_element(*Confirm.confirm_cb)

    def btn_purchase_click(self):
        return self.driver.find_element(*Confirm.btn_purchase)

    def msg_success(self):
        return self.driver.find_element(*Confirm.txt_success)


