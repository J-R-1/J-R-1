import pytest
from selenium.webdriver.support.select import Select

from TestData import Homepagedata
from TestdataPkg.HomepageData import HomepageData
from pageObjects.homePage import HomePage
from startUP.baseClass import BaseClass


class TestHomePage(BaseClass):
    def test_homepageForm(self, getData):
        log = self.getLogger()
        log.info('Entering Info @HomePage')

        obj_formHomepage = HomePage(self.driver)
        obj_formHomepage.getFormName().send_keys(getData["FName"])
        obj_formHomepage.getFormEmail().send_keys(getData["Email"])
        obj_formHomepage.getFormPwd().send_keys(getData["Pwd"])
        obj_formHomepage.clickFormCheckBox1().click()
#        sel = Select(obj_formHomepage.getFormGender())
#        sel.select_by_visible_text('Male')
        self.selectStaticDropdown(obj_formHomepage.getFormGender(), getData["Gender"])
        obj_formHomepage.clickFormSubmitBtn().click()

        successText = obj_formHomepage.getFormSuccessMsg().text
        log.info('HomePage execution is successful' +successText)

        assert 'Success!' in successText
        self.driver.refresh()


    @pytest.fixture(params=HomepageData.get_homepageData('TestCase1'))
    def getData(self, request):
        return request.param







