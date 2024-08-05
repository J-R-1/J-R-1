from selenium.webdriver.common.by import By

from pageObjects.checkoutPage import CheckOut


class HomePage:

    def __init__(self, driver):
        self.driver = driver


    shop = (By.LINK_TEXT, 'Shop')
    name = (By.CSS_SELECTOR, 'input[name="name"]')
    email = (By.CSS_SELECTOR, 'input[name="email"]')
    pwd = (By.CSS_SELECTOR, '#exampleInputPassword1')
    checkBox1 = (By.CSS_SELECTOR, '#exampleCheck1')
    gender = (By.CSS_SELECTOR, '#exampleFormControlSelect1')
    submitBtn = (By.CSS_SELECTOR, 'input[type="submit"]')
    successMsg = (By.CLASS_NAME, 'alert-success')


    def shopitem(self):
#        return self.driver.find_element(*HomePage.shop)
         self.driver.find_element(*HomePage.shop).click()
         checkout_Obj = CheckOut(self.driver)
         return checkout_Obj

    def getFormName(self):
        return self.driver.find_element(*HomePage.name)

    def getFormEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getFormPwd(self):
        return self.driver.find_element(*HomePage.pwd)

    def clickFormCheckBox1(self):
        return self.driver.find_element(*HomePage.checkBox1)

    def getFormGender(self):
        return self.driver.find_element(*HomePage.gender)

    def clickFormSubmitBtn(self):
        return self.driver.find_element(*HomePage.submitBtn)


    def getFormSuccessMsg(self):
        return self.driver.find_element(*HomePage.successMsg)

