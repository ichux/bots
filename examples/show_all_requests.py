import sys
import time

from selenium.common.exceptions import WebDriverException

from executes.browser import Driver


# noinspection PyProtectedMember
def get_data():
    """
    Aborts .css files and adverts linking to some pages
    :return:
    """
    # driver = Driver.phantomjs()
    # driver.command_executor._commands['executePhantomScript'] = ('POST', '/session/$sessionId/phantom/execute')
    #
    # script = """
    # var page = this;
    #
    # page.onResourceReceived = function(response) {
    #   console.log('response: ' + JSON.stringify(response));
    #   console.log('(#' + response.id + ', stage "' + response.stage + '": ' + response.url + ' ' + JSON.stringify(response.headers));
    # };
    #
    # page.onResourceRequested = function (requestData, networkRequest) {
    #     var hidden = (.css).test(requestData['url']);
    #     if ((/http:\/\/.+?\.css$/gi).test(requestData['url']) || hidden) {
    #         console.log('[PhantomJS] Request (#' + requestData.id + '): ' + requestData.url + ' -> abort');
    #         networkRequest.abort();
    #     }
    #
    #     if (/googlesyndication.com|doubleclick.net|google-analytics.com/.test(requestData['url'])) {
    #         console.log('[PhantomJS] Request (#' + requestData.id + '): ' + requestData.url + ' -> abort');
    #         networkRequest.abort();
    #     }
    # };
    # """.strip()
    #
    # # check ghostdriver.log file for the result of the statement below
    # driver.execute('executePhantomScript', {'script': script, 'args': []})
    #
    # try:
    #     driver.get("https://radar.techcabal.com/")
    #
    #     time.sleep(5)  # allows for proper load on some either slow network or resource intensive webpage
    #     driver.save_screenshot("radar-tech-cabal.png")
    # except WebDriverException as exc:
    #     driver.save_screenshot("radar-tech-cabal-exception.png")
    #     print("WebDriverException: {} {}".format(exc, sys.exc_info()[0]))
    # except (Exception,) as exc:
    #     print("Exception: {} {}".format(exc, sys.exc_info()[0]))
    # finally:
    #     driver.quit()
    pass


if __name__ == '__main__':
    get_data()
