from selenium.webdriver.common.by import By

#from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.checkoutPage import CheckOut
from pageObjects.confirmPage import Confirm
from pageObjects.homePage import HomePage
from startUP.baseClass import BaseClass


#@pytest.mark.usefixtures('setup')
class Test_e2e(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        log.info('Entering and Executing e2e test')
        obj_homePage = HomePage(self.driver)


# collecting all the elements

        obj_checkOut = obj_homePage.shopitem()

        pLists = obj_checkOut.prodList()


        prodNames = []
        log.info('Getting the Prod Info')

        for prod in pLists:
            prodName = prod.find_element(By.XPATH, 'div/h4/a').text
            if prodName == 'Blackberry':
                prod.find_element(By.XPATH, 'div/button').click()



        log.info('Getting out from Checkout page by clicking CheckOut btn')


        obj_checkOut.btn_Click_Checkout().click()

        # display total amt

        totAmt = obj_checkOut.Check_tot_amt().text
        log.info('Total amt' + totAmt)



        #confirm Page:
#        obj_confirm = Confirm(self.driver)
        obj_confirm = obj_checkOut.btn_Success_Checkout()
        log.info('Entering country name as Po')
        obj_confirm.dropdown_find_country().send_keys('Po')

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="suggestions"]//a[text()="Portugal"]'))).click()



        obj_confirm.click_confirm().click()
        log.info('Confirm Btn clicked')

        obj_confirm.btn_purchase_click().click()


        successText = obj_confirm.msg_success().text

        log.info('Retrieving the Success text' +successText)

        assert "Success!" in successText

