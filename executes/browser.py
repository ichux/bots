import os

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from executes import PHANTOMJS, QUICKJAVA, CHROME, LOGIT, GECKODRIVER


class Driver:
    def __init__(self):
        pass

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
        # browser = webdriver.Chrome(chrome_options=co)
        #

        os.environ["webdriver.chrome.driver"] = CHROME

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('disable-notifications')

        # chrome_options.binary_location = os.path.join(EXECUTABLE_PATH, 'drivers')

        if headless:
            chrome_options.add_argument('headless')

        if not image:
            chrome_options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        return webdriver.Chrome(executable_path=CHROME, chrome_options=chrome_options)

    @staticmethod
    def firefox(image=False):
        """
        Get a prepared Firefox driver.
        :param image: a boolean value used in indicating if you want images to show or not
        :return: the prepared webdriver instance
        """
        profile = webdriver.FirefoxProfile()

        # profile.set_preference("webdriver.log.file", "/tmp/firefox_console")
        profile.add_extension(QUICKJAVA)

        # Prevents loading the 'thank you for installing screen'. It has to be the version of the plugin
        profile.set_preference("thatoneguydotnet.QuickJava.curVersion", "2.1.0")

        if not image:
            # 0 = no change, 1 = enabled, 2 = disabled
            profile.set_preference("thatoneguydotnet.QuickJava.startupStatus.AnimatedImage", 2)
            profile.set_preference("thatoneguydotnet.QuickJava.startupStatus.Images", 2)

        """
        FirefoxProfile myprofile=new FirefoxProfile();
        myprofile.setPreference("browser.download.folderList", 2);
        myprofile.setPreference("browser.download.manager.showWhenStarting", false);
        myprofile.setPreference("browser.download.dir", downloadPath);
        myprofile.setPreference("browser.helperApps.neverAsk.openFile","application/msword, application/csv, application/ris, text/csv, image/png, application/pdf, text/html, text/plain, application/zip, application/x-zip, application/x-zip-compressed, application/download, application/octet-stream");
        myprofile.setPreference("browser.helperApps.neverAsk.saveToDisk", "application/msword, application/csv, application/ris, text/csv, image/png, application/pdf, text/html, text/plain, application/zip, application/x-zip, application/x-zip-compressed, application/download, application/octet-stream");
        myprofile.setPreference("browser.helperApps.alwaysAsk.force", false);
        myprofile.setPreference("browser.download.manager.showAlertOnComplete", false);
        myprofile.setPreference("browser.download.manager.closeWhenDone", false);
        """

        # profile.set_preference("thatoneguydotnet.QuickJava.startupStatus.Flash", 2)
        # profile.set_preference("thatoneguydotnet.QuickJava.startupStatus.Silverlight", 2)
        # profile.set_preference("thatoneguydotnet.QuickJava.startupStatus.JavaScript", 0)
        # profile.set_preference("thatoneguydotnet.QuickJava.startupStatus.Java", 0)
        # profile.set_preference("thatoneguydotnet.QuickJava.startupStatus.WebGL", 0)
        # profile.set_preference("thatoneguydotnet.QuickJava.startupStatus.WebRTC", 0)
        # profile.set_preference("thatoneguydotnet.QuickJava.startupStatus.Cookies", 0)
        # profile.set_preference("thatoneguydotnet.QuickJava.startupStatus.CSS", 0)
        # profile.set_preference("thatoneguydotnet.QuickJava.startupStatus.Proxy", 0)

        return webdriver.Firefox(firefox_profile=profile, executable_path=GECKODRIVER)

    @staticmethod
    def phantomjs(image=False, filename=None):
        """
        Get a prepared PhantomJS driver.
        :param image: a boolean value used in indicating if you want images to show or not
        :param filename: a string which indicates the directory to store the logs
        :return: the prepared webdriver instance
        """
        user_agent = (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/53.0.2785.116 Safari/537.36")

        capabilities = DesiredCapabilities.PHANTOMJS.copy()
        capabilities["phantomjs.page.settings.userAgent"] = user_agent

        if not image:
            capabilities["phantomjs.page.settings.loadImages"] = False
        # capabilities["phantomjs.cli.args"] = ['--cookies-file=ifindam/products/hacks/logs/cookies.txt']

        if filename is None:
            filename = os.path.join(LOGIT, 'ghostdriver.log')
            # print("filename = {}".format(filename))

        service_args = ['--ignore-ssl-errors=true', '--ssl-protocol=any', '--web-security=false']
        service_args += ['--disk-cache=true', '--disk-cache-path={}'.format(LOGIT)]
        service_args += ['--local-to-remote-url-access=true']
        # service_args += ['--cookies-file={}'.format(os.path.join(LOGIT, 'cookies.txt'))]

        return webdriver.PhantomJS(desired_capabilities=capabilities, service_args=service_args,
                                   executable_path=PHANTOMJS, service_log_path=filename)
