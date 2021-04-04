import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from executes import error_logs
from executes.browser import Driver


class TestDDG(unittest.TestCase):
    def setUp(self):
        self.driver = Driver.remote_chrome()
        self.driver.set_window_size(1920, 1080)
        self.driver.maximize_window()

        self.search_url = "https://duckduckgo.com/?q=zuoike+ichux"

    @error_logs
    def test_ddg(self):
        self.driver.get("http://duckduckgo.com/")

        self.driver.find_element_by_id('search_form_input_homepage').send_keys("zuoike ichux")
        self.driver.find_element_by_id("search_button_homepage").click()

        self.assertIn(self.search_url, self.driver.current_url)

        links_wrapper = self.driver.find_element_by_css_selector("div#links_wrapper.serp__results.js-serp-results")

        with open("test_ddg.png", "wb") as elem_file:
            elem_file.write(links_wrapper.screenshot_as_png)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
