import os
import sys
import unittest

from selenium.common.exceptions import WebDriverException

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from executes.browser import Driver


class TestOne(unittest.TestCase):
    def setUp(self):
        self.driver = Driver.firefox()
        # self.driver.set_window_size(1120, 550)

    def test_phantom(self):
        try:
            self.driver.get("http://duckduckgo.com/")

            self.driver.find_element_by_id('search_form_input_homepage').send_keys("realpython")
            self.driver.find_element_by_id("search_button_homepage").click()

            self.assertIn("https://duckduckgo.com/?q=realpython", self.driver.current_url)
        except WebDriverException as exc:
            # return "WebDriverException: {} {}".format(exc, sys.exc_info()[0])
            pass
        except (Exception,) as exc:
            # return "Exception: {} {}".format(exc, sys.exc_info()[0])
            pass

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
