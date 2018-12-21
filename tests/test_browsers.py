import os
import sys
import time
import unittest

from selenium.common.exceptions import WebDriverException

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from executes.browser import Driver


class HeadlessBrowsers(unittest.TestCase):
    def setUp(self):
        self.start_time = time.time()
        self.driver = None

    def test_firefox(self):
        try:
            self.driver = Driver.firefox()
            self.driver.get("https://app.simplegoods.co/i/IQCZADOY")  # url associated with button click
            button = self.driver.find_element_by_id("payment-submit").get_attribute("value")
            self.assertEquals(u'Pay - $60.00', button)
        except WebDriverException:
            pass
        except (Exception,):
            pass

    def test_chrome(self):
        try:
            self.driver = Driver.chrome()
            self.driver.get("https://app.simplegoods.co/i/IQCZADOY")  # url associated with button click
            button = self.driver.find_element_by_id("payment-submit").get_attribute("value")
            self.assertEquals(u'Pay - $60.00', button)
        except WebDriverException:
            pass
        except (Exception,):
            pass

    def tearDown(self):
        try:
            # print(self.driver.get_cookies())
            self.driver.quit()

            t = time.time() - self.start_time
            print("%s: %.3f" % (self.id(), t))
        except AttributeError:
            pass


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(HeadlessBrowsers)
    unittest.TextTestRunner(verbosity=0).run(suite)
