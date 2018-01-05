import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from . import Getbrowser

class PythonOrgSearch(unittest.TestCase):

    def setUp(self): #Start the browser
        self.driver = Getbrowser.Chrome()

    def test_search_in_python_org(self): #Should start with the word "test" that test case can be ran
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self): #Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
