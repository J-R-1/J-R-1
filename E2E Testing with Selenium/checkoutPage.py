#prodList = self.driver.find_elements(By.XPATH, '//div[@class="card h-100"]')
#prod.find_element(By.XPATH, 'div/h4/a').text
#prod.find_element(By.XPATH, 'div/button').click()
#self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
#self.driver.find_element(By.XPATH, '//tr/td[@class="text-right"]/h3/strong').text
#self.driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-success"]').click()
from selenium.webdriver.common.by import By

from pageObjects.confirmPage import Confirm


class CheckOut():

    def __init__(self, driver):
        self.driver = driver

    prod_List = (By.XPATH, '//div[@class="card h-100"]')
    prod_name = (By.XPATH, 'div/h4/a')
    prod_click = (By.XPATH, 'div/button')
    btn_CheckOut_click = (By.XPATH, '//a[@class="nav-link btn btn-primary"]')
    tot_amt = (By.XPATH, '//tr/td[@class="text-right"]/h3/strong')
    btn_Checkout_success = (By.CSS_SELECTOR, 'button[class="btn btn-success"]')

    def prodList(self):
        return self.driver.find_elements(*CheckOut.prod_List)

    def prodname(self):
        return self.driver.find_element(*CheckOut.prod_name)

    def prod_blkberry(self):
        return self.driver.find_element(*CheckOut.prod_click)

    def btn_Click_Checkout(self):
        return self.driver.find_element(*CheckOut.btn_CheckOut_click)

    def Check_tot_amt(self):
        return self.driver.find_element(*CheckOut.tot_amt)

    def btn_Success_Checkout(self):
 #       return self.driver.find_element(*CheckOut.btn_Checkout_success)
         self.driver.find_element(*CheckOut.btn_Checkout_success).click()
         confirmpage_Obj = Confirm(self.driver)
         return confirmpage_Obj
