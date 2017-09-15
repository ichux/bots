import os
import sys

from selenium.common.exceptions import WebDriverException

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from executes.browser import Driver

LOCATION = os.path.realpath(os.path.dirname(os.path.realpath(__file__)))


def stringify(intake):
    """
    Takes a valid JSON as input and emits it in valid string format
    PhantomJS in this case will not emit a log file
    :param intake: the valid string.
    :return: a valid JSON string format. Else, the exception message is returned
    """
    driver = Driver.phantomjs(filename=os.path.devnull)

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


if __name__ == '__main__':
    print(stringify('{"gmt_time":new Date()}'))
