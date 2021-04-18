import os
import warnings
from contextlib import contextmanager

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from executes import CHROME, GECKODRIVER, LOGGER

SELENIUM_URL = os.getenv('SELENIUM_URL')
PROXY = os.getenv('PROXY')


@contextmanager
def chrome(*args, **kwargs):
    args, exception = args, False

    if args == 'rc':
        drv = Driver.remote_chrome(**kwargs)
    else:
        drv = Driver.chrome(**kwargs)

    try:
        yield drv
    except WebDriverException as exc:
        exception = True
        LOGGER.exception(f"WebDriverException: {exc}")
    except (Exception,) as exc:
        exception = True
        LOGGER.exception(f"Exception: {exc}")
    finally:
        drv.quit()

        if exception:
            raise


class Driver(object):
    @staticmethod
    def remote_chrome(image=True, headless=False):
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        driver = Driver._remote_chrome(image, headless)
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        return driver

    @staticmethod
    def _remote_chrome(image=True, headless=False):
        """
        Get a prepared Chrome driver.
        :param headless: indicates if the browser will run in headless mode or not
        :param image: change it to False once you don't want images shown
        :return: the prepared webdriver instance
        """
        chrome_options = Driver.chrome_options()

        if PROXY:
            chrome_options.add_argument(f'--proxy-server={PROXY}')

        # Note: `headless = True` and `image is False` get detected by Instagram
        # Do use them with caution as some sites might detect these features and
        # Activate their panic mode

        if headless:
            chrome_options.headless = True

        if image is False:
            chrome_options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})

        return webdriver.Remote(SELENIUM_URL, DesiredCapabilities.CHROME, options=chrome_options)

    @staticmethod
    def chrome(image=False, headless=True):
        """
        Get a prepared Chrome driver.
        :param headless: indicates if you want it to appear as headless or not
        :param image: a boolean value used in indicating if you want images to show or not
        :return: the prepared webdriver instance
        """

        # co = webdriver.ChromeOptions()
        # co.add_argument("--user-data-dir=userdir")
        # browser = webdriver.Chrome(options=co)
        #

        os.environ["webdriver.chrome.driver"] = CHROME
        options = Driver.chrome_options()

        # options.binary_location = os.path.join(EXECUTABLE_PATH, 'drivers')

        if headless:
            options.add_argument('headless')

        if not image:
            options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        return webdriver.Chrome(executable_path=CHROME, options=options)

    @staticmethod
    def firefox():
        """
        Get a prepared Firefox driver.
        :return: the prepared webdriver instance
        """
        profile = webdriver.FirefoxProfile()
        #
        # # profile.set_preference("webdriver.log.file", "/tmp/firefox_console")
        # profile.add_extension(QUICK_JAVA)
        #
        # # Prevents loading the 'thank you for installing screen'. It has to be the version of the plugin
        # profile.set_preference("thatoneguydotnet.QuickJava.curVersion", "2.1.0")
        #
        # if not image:
        #     # 0 = no change, 1 = enabled, 2 = disabled
        #     profile.set_preference("thatoneguydotnet.QuickJava.startupStatus.AnimatedImage", 2)
        #     profile.set_preference("thatoneguydotnet.QuickJava.startupStatus.Images", 2)

        return webdriver.Firefox(firefox_profile=profile, executable_path=GECKODRIVER)

    @staticmethod
    def chrome_options():
        options = webdriver.ChromeOptions()
        options.add_argument('incognito')
        options.add_argument('disable-notifications')
        options.add_argument('ignore-certificate-errors')
        options.add_argument("no-sandbox")
        options.add_argument("--disable-gpu")

        # options.add_argument("--window-size=800,600")
        # options.add_argument("--start-maximized")

        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-crash-reporter")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-in-process-stack-traces")
        options.add_argument("--disable-logging")
        options.add_argument("--log-level=3")

        return options
