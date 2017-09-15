import sys
import time
import os

from selenium.common.exceptions import WebDriverException

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from executes.browser import Driver


# noinspection PyProtectedMember
def get_data():
    """
    Aborts .css files and adverts linking to some pages
    :return:
    """
    driver = Driver.phantomjs()
    driver.command_executor._commands['executePhantomScript'] = ('POST', '/session/$sessionId/phantom/execute')

    script = """
    var page = this;
    
    var skip = ['googleads.g.doubleclick.net', 'cm.g.doubleclick.net', 'www.googleadservices.com'];
    skip.push.apply(skip, ['googlesyndication.com', 'doubleclick.net', 'google-analytics.com']);

    page.onResourceRequested = function (requestData, networkRequest) {
        if (requestData.url.indexOf(".css") > -1) {
            console.log('Request (#' + requestData.id + '): ' + requestData.url + ' -> abort');
            networkRequest.abort();
        }
    
        skip.forEach(function (needle) {
            if (requestData.url.indexOf(needle) > 0) {
                networkRequest.abort();
            }
        });
    
        // if (/googlesyndication.com|doubleclick.net|google-analytics.com/.test(requestData.url)) {
        //     console.log('Request (#' + requestData.id + '): ' + requestData.url + ' -> abort');
        //     networkRequest.abort();
        // }
    };
    """.strip()

    # check ghostdriver.log file for the result of the statement below
    driver.execute('executePhantomScript', {'script': script, 'args': []})

    try:
        driver.get("https://radar.techcabal.com/")

        time.sleep(5)  # allows for proper load on some either slow network or resource intensive webpage
        driver.save_screenshot("radar-tech-cabal.png")
    except WebDriverException, e:
        driver.save_screenshot("radar-tech-cabal-exception.png")
        print("WebDriverException: {} {}".format(e, sys.exc_info()[0]))
    except (Exception,), e:
        print("Exception: {} {}".format(e, sys.exc_info()[0]))
    finally:
        driver.quit()


if __name__ == '__main__':
    get_data()
