import os
import sys
import time
import unittest
import warnings

from seleniumwire import webdriver

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from executes import error_logs, CHROME


class TestUndetectableChrome(unittest.TestCase):
    def setUp(self):
        self.start_time = time.time()

        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
        self.driver = webdriver.Chrome(executable_path=CHROME, options=options)
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        self.url = 'https://intoli.com/blog/making-chrome-headless-undetectable/chrome-headless-test.html'

    @error_logs
    def test_detection(self):
        self.driver.get(self.url)

        # Access requests via the `requests` attribute
        for request in self.driver.requests:
            if request.response:
                # print(
                #     request.url,
                #     request.response.status_code,
                #     request.response.headers['Content-Type']
                # )

                if self.url == request.url:
                    self.assertEqual(self.url, request.url)

        table = self.driver.find_element_by_css_selector("body > table:nth-child(1)")

        with open("test_detection.png", "wb") as elem_file:
            elem_file.write(table.screenshot_as_png)

    def test_screen_size(self):
        intake = """\
        var w = window, 
        d = document, 
        e = d.documentElement, 
        g = d.getElementsByTagName('body')[0], 
        x = w.innerWidth || e.clientWidth || g.clientWidth, y = w.innerHeight|| e.clientHeight|| g.clientHeight;

        return x + ' × ' + y
        """

        self.driver.get(url="file:///")
        response = self.driver.execute_script(intake)

        self.assertIn(' × ', response)
        self.driver.get_screenshot_as_file('test_screen_size.png')

    def tearDown(self):
        try:
            # print(self.driver.get_cookies())
            self.driver.quit()
            print("%s: %.3f" % (self.id(), time.time() - self.start_time))
        except AttributeError:
            pass
