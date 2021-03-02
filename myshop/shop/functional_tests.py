from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('This amazing shop', self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Items', header_text)

        footer_div = self.browser.find_elements_by_class_name('footer')
        self.assertIn('footer', footer_div)
