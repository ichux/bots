import io
import os
import sys
import time
import unittest

from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from executes.browser import Driver
from executes import error_logs


class TestHeadlessBrowsers(unittest.TestCase):
    def setUp(self):
        self.start_time = time.time()
        self.driver = None

    def test_time(self):
        self.driver = Driver.chrome()

        intake = """
        var now = new Date();
        return JSON.stringify({"gmt_time":now, "epoch":now.getTime()}, undefined, 4) || null;
        """

        self.driver.get(url="file:///")
        response = self.driver.execute_script(intake)

        self.assertIn("epoch", response)

    def test_js_call(self):
        self.driver = Driver.chrome()
        self.driver.get(url="file:///")

        intake = '{"gmt_time":new Date()}'
        response = self.driver.execute_script('return JSON.stringify({0}, undefined, 2) || null;'.format(intake))

        # self.driver.get_screenshot_as_file('test_js_call.png')

        self.assertIn("gmt_time", response)

    @error_logs
    def test_bounding_rect(self):
        intake = """clipRect = document.querySelector("div.home-quote").getBoundingClientRect();
        dicts = {left_x:   clipRect.left,
        top_y: clipRect.top, width:  clipRect.width,
        height: clipRect.height
        };
        
        return JSON.stringify(dicts, undefined, 2);
        """

        self.driver = Driver.chrome()
        self.driver.get(url="https://wingware.com/")

        response = self.driver.execute_script(intake)
        self.assertIn("top", response)

    @error_logs
    def test_bounding_rect_save(self):
        self.driver = Driver.chrome()

        self.driver.set_window_size(1920, 1080)
        self.driver.maximize_window()

        self.driver.get(url="https://wingware.com/")

        home_quote = self.driver.find_element_by_css_selector("div.home-quote")

        with open("test_bounding_rect_save.png", "wb") as elem_file:
            elem_file.write(home_quote.screenshot_as_png)

    @error_logs
    def test_body_save_buffer(self):
        self.driver = Driver.chrome()

        self.driver.set_window_size(1920, 1080)
        self.driver.maximize_window()

        self.driver.get(url="https://wingware.com/")

        element = self.driver.find_element_by_css_selector("body")

        image_stream = io.BytesIO(element.screenshot_as_png)
        im = Image.open(image_stream)

        home_quote = self.driver.find_element_by_css_selector("div.home-quote")
        location = home_quote.location
        size = home_quote.size

        x, y = int(location['x']), int(location['y'])
        width, height = int(location['x'] + size['width']), int(location['y'] + size['height'])

        im = im.crop((x, y, width, height))
        im.save('test_body_save_buffer.png')

    def tearDown(self):
        try:
            # print(self.driver.get_cookies())
            self.driver.quit()
            print("%s: %.3f" % (self.id(), time.time() - self.start_time))
        except AttributeError:
            pass


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHeadlessBrowsers)
    unittest.TextTestRunner(verbosity=0).run(suite)
