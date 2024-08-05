import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service

#google command line options pytest -> https://docs.pytest.org/en/7.1.x/example/simple.html
#cmd -> py.test --browser_name Edge
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="Edge"
    )



@pytest.fixture(scope='class')
def setup(request):
    browserName = request.config.getoption("--browser_name")
    obj_ser = Service()

    if browserName == 'Edge':
        edgeOption = webdriver.EdgeOptions()
        edgeOption.add_argument("--start-maximized")
        driver = webdriver.Edge(service=obj_ser, options=edgeOption)
    elif browserName == 'Chrome':
        chromeOption = webdriver.ChromeOptions()
        chromeOption.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=obj_ser, options=chromeOption)


    driver.get('https://www.rahulshettyacademy.com/angularpractice/')
    request.cls.driver = driver
    yield
    driver.close()