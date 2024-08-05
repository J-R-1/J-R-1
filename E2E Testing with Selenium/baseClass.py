import inspect
import logging

import pytest
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures('setup')
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]

        logger = logging.getLogger(loggerName)

        filehandler = logging.FileHandler('logFile.log')

        format = logging.Formatter('%(asctime)s :%(levelname)s :%(name)s :%(message)s')

        filehandler.setFormatter(format)

        if logger.hasHandlers():
            logger.handlers.clear()

        logger.addHandler(filehandler)

        logger.setLevel(logging.DEBUG)

        #logger.debug('Debug statment will be printed')
        #logger.info('Info statment will be printed')
        #logger.warning('Warning stat will be printed')
        #logger.error('Error statment will be printed')
        #logger.critical('Critical statments will be printed')
        return logger

    def selectStaticDropdown(self, locator, value):
        sel = Select(locator)
        sel.select_by_visible_text(value)