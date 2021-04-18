import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from executes.browser import chrome


class TestDDG(unittest.TestCase):
    def setUp(self):
        self.search_url = "https://duckduckgo.com/?q=zuoike+ichux"

    def test_ddg(self):
        with chrome('rc') as driver:
            driver.set_window_size(1920, 1080)
            driver.maximize_window()

            driver.get("http://duckduckgo.com/")

            driver.find_element_by_id('search_form_input_homepage').send_keys("zuoike ichux")
            driver.find_element_by_id("search_button_homepage").click()

            self.assertIn(self.search_url, driver.current_url)

            links_wrapper = driver.find_element_by_css_selector("div#links_wrapper.serp__results.js-serp-results")

            with open("test_ddg.png", "wb") as elem_file:
                elem_file.write(links_wrapper.screenshot_as_png)


if __name__ == '__main__':
    unittest.main()
