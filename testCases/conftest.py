from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("Launching Chrome browser....")
    elif browser=='firefox':
        driver=webdriver.Firefox()
        print("Launching Firefox browser....")
    else:
        driver=webdriver.Ie()
    return driver


    return driver

def pytest_addoption(parser): #This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #This will return the Browser value to setup method
    return request.config.getoption("--browser")

#############PyTest HTML Report########################
#It is a hook for adding environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Sreedevi'

#It is a hook for deleting/Modify environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)
