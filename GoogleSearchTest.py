from selenium import webdriver
import unittest

class GoogleSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_automaticnsstepbysep(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Current stock")
        self.driver.find_element_by_name("btnK").click()

   @classmethod
   def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")