import os
import sys

from selenium.common.exceptions import WebDriverException

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from executes.browser import Driver


def stringify(intake):
    """
    Takes a valid JSON as input and emits it in valid string format
    :param intake: the valid string.
    :return: a valid JSON string format. Else, the exception message is returned
    """
    driver = Driver.phantomjs()  # Driver.firefox(), Driver.chrome(headless=False)

    try:
        driver.get(url="file:///")
        # return driver.execute_script('return JSON.stringify({0}) || null;'.format(intake))
        return driver.execute_script('return JSON.stringify({0}, undefined, 4) || null;'.format(intake))
    except WebDriverException, e:
        return "WebDriverException: {} {}".format(e, sys.exc_info()[0])
    except (Exception,), e:
        return "Exception: {} {}".format(e, sys.exc_info()[0])
    finally:
        driver.quit()


def tell_time():
    """
    Shows the time in GMT
    :return: a string. Else, the exception message is returned
    """
    driver = Driver.phantomjs()

    intake = """
    var now = new Date();
    return JSON.stringify({"gmt_time":now, "epoch":now.getTime()}, undefined, 4) || null;
    """.strip()

    try:
        driver.get(url="file:///")
        return driver.execute_script("{0}".format(intake))
    except WebDriverException, e:
        return "WebDriverException: {} {}".format(e, sys.exc_info()[0])
    except (Exception,), e:
        return "Exception: {} {}".format(e, sys.exc_info()[0])
    finally:
        driver.quit()


if __name__ == '__main__':
    print(stringify('{"gmt_time":new Date()}'))
    print(tell_time())
