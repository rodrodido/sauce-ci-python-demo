from selenium import webdriver
import unittest, time, re
import os
import json


"""
"""
class testSauceWrappers(unittest.TestCase):
    username = "rossco_9_9"
    access_key = "44f0744c-1689-4418-af63-560303cbb37b"
    def setUp(self):
        desired_capabilities = {}
		desired_capabilities['browser'] = os.environ['SELENIUM_BROWSER']              
        desired_capabilities['version'] = os.environ['SELENIUM_VERSION'] 
        desired_capabilities['platform'] = os.environ['SELENIUM_PLATFORM']
       
       command_executor="http://%s:%s@%s:%s/wd/hub"%(os.environ['SAUCE_USER_NAME'], os.environ['SAUCE_API_KEY'], os.environ['SELENIUM_HOST'], os.environ['SELENIUM_PORT'])

       #make sure the test doesn't run forever if if the test crashes
       if parse.getMaxDuration() != 0:
           desired_capabilities['max-duration'] = parse.getMaxDuration()
           desired_capabilities['command-timeout'] = parse.getMaxDuration()

       if parse.getIdleTimeout() != 0:
           desired_capabilities['idle-timeout'] = parse.getIdleTimeout()

       driver=webdriver.Remote(desired_capabilities=desired_capabilities, command_executor=command_executor)

    def retrieve_job_details(self, browser):
        sauceRest = SauceRest(self.username, self.access_key)
        result = sauceRest.get(browser.id())
        data = json.loads(result)
        return data

    def test_webdriver_success(self):

        browser = SeleniumFactory().createWebDriver()
        browser.get("http://amazon.com")
        assert "Amazon.com" in browser.title
        browser.job_passed()
        data = self.retrieve_job_details(browser)
        assert data['passed']
        browser.quit()

    def test_webdriver_failed(self):

        browser = SeleniumFactory().createWebDriver()
        browser.get("http://amazon.com")
        assert "Amazon.com" in browser.title
        browser.job_failed()
        data = self.retrieve_job_details(browser)
        assert not data['passed']
        browser.quit()

    def test_selenium_success(self):
        browser = SeleniumFactory().create()
        browser.open("http://www.amazon.com")
        assert "Amazon.com" in browser.get_title()
        browser.job_passed()
        data = self.retrieve_job_details(browser)
        assert data['passed']
        browser.stop()

    def test_selenium_failed(self):
        browser = SeleniumFactory().create()
        browser.open("http://www.amazon.com")
        assert "Amazon.com" in browser.get_title()
        browser.job_failed()
        data = self.retrieve_job_details(browser)
        assert not data['passed']
        browser.stop()

if __name__ == "__main__":
    unittest.main()