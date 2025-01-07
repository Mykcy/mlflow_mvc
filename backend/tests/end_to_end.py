import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestHomePage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_home_page(self):
        self.driver.get('http://localhost:5000')
        self.assertIn('Hello, World!', self.driver.page_source)

class TestFileUpload(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_file_upload(self):
        self.driver.get('http://localhost:5000/upload')
        upload_element = self.driver.find_element(By.NAME, 'file')
        upload_element.send_keys('/path/to/your/file.txt')
        upload_element.send_keys(Keys.RETURN)
        self.assertIn('File uploaded successfully', self.driver.page_source)

class TestMLflowIntegration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_mlflow_integration(self):
        self.driver.get('http://localhost:5000/log')
        param_input = self.driver.find_element(By.NAME, 'param1')
        metric_input = self.driver.find_element(By.NAME, 'metric1')
        param_input.send_keys('value1')
        metric_input.send_keys('0.5')
        param_input.send_keys(Keys.RETURN)
        self.assertIn('Logged successfully', self.driver.page_source)
if __name__ == '__main__':
    unittest.main()





