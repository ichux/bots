import io
import os
import sys
import time
import unittest

from PIL import Image
from pathlib import Path
from selenium.webdriver.common.by import By
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from executes.browser import chrome


class TestHeadlessBrowsers(unittest.TestCase):
    def setUp(self):
        self.start_time = time.time()
        self.url = "https://wingware.com/"

    def test_time(self):
        with chrome(image=False, headless=True) as driver:
            intake = """
            var now = new Date();
            return JSON.stringify({"gmt_time":now, "epoch":now.getTime()}, undefined, 4) || null;
            """
    
            driver.get(url="file:///")
            response = driver.execute_script(intake)
    
            self.assertIn("epoch", response)

    def test_js_call(self):
        with chrome(image=False, headless=True) as driver:
            driver.get(url="file:///")

            intake = '{"gmt_time":new Date()}'
            response = driver.execute_script('return JSON.stringify({0}, undefined, 2) || null;'.format(intake))

            self.assertIn("gmt_time", response)

    def test_bounding_rect(self):
        intake = """clipRect = document.querySelector("div.home-quote").getBoundingClientRect();
        dicts = {left_x:   clipRect.left,
        top_y: clipRect.top, width:  clipRect.width,
        height: clipRect.height
        };
        
        return JSON.stringify(dicts, undefined, 2);
        """

        with chrome(image=False, headless=True) as driver:
            driver.get(url=self.url)

            response = driver.execute_script(intake)
            self.assertIn("top", response)

    def test_bounding_rect_save(self):
        with chrome(image=False, headless=True) as driver:

            driver.set_window_size(1920, 1080)
            driver.maximize_window()

            driver.get(url=self.url)

            home_quote = driver.find_element(by=By.CSS_SELECTOR, value="div.home-quote")

            with open("test_bounding_rect_save.png", "wb") as elem_file:
                elem_file.write(home_quote.screenshot_as_png)

    def test_body_save_buffer(self):
        with chrome(image=False, headless=True) as driver:
            driver.set_window_size(1920, 1080)
            driver.maximize_window()

            driver.get(url=self.url)

            element = driver.find_element(by=By.CSS_SELECTOR, value="body")

            image_stream = io.BytesIO(element.screenshot_as_png)
            im = Image.open(image_stream)

            home_quote = driver.find_element(by=By.CSS_SELECTOR, value="div.home-quote")
            location = home_quote.location
            size = home_quote.size

            x, y = int(location['x']), int(location['y'])
            width, height = int(location['x'] + size['width']), int(location['y'] + size['height'])

            im = im.crop((x, y, width, height))
            im.save('test_body_save_buffer.png')

    def tearDown(self):
        print(f"{self.id()}: {(time.time() - self.start_time):.4f}s")


if __name__ == '__main__':
    unittest.main()
