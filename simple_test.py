from selenium import webdriver
import unittest
import os


"""
Python unittest class which demonstrates creating a webdriver instance using environment variables
populated by the Sauce CI plugins.
"""

class testSauceWrappers(unittest.TestCase):

    def setUp(self):
        desired_capabilities = {}
        desired_capabilities['browserName'] = os.environ['SELENIUM_BROWSER']
        if (os.environ['SELENIUM_VERSION'])
            desired_capabilities['version'] = os.environ.get['SELENIUM_VERSION']
        desired_capabilities['platform'] = os.environ['SELENIUM_PLATFORM']
        command_executor = "http://%s:%s@%s:%s/wd/hub" % (os.environ['SAUCE_USER_NAME'], os.environ['SAUCE_API_KEY'], os.environ['SELENIUM_HOST'], os.environ['SELENIUM_PORT'])
        self.driver = webdriver.Remote(desired_capabilities=desired_capabilities, command_executor=command_executor)


    def test_amazon(self):
        driver = self.driver
        driver.get("http://amazon.com")
        print "\rSauceOnDemandSessionID=%s job-name=%s" % (self.driver.session_id, "test_amazon")
        assert "Amazon.com" in driver.title
        driver.quit()


if __name__ == "__main__":
    unittest.main()
