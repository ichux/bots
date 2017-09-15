import sys
import time

from selenium.common.exceptions import WebDriverException

from executes.browser import Driver


# noinspection PyProtectedMember
def get_data():
    driver = Driver.phantomjs()
    driver.command_executor._commands['executePhantomScript'] = ('POST', '/session/$sessionId/phantom/execute')

    script = """
    var page = this;

    //page.onResourceReceived = function(response) {
      // console.log('response: ' + JSON.stringify(response));
    //  console.log('(#' + response.id + ', stage "' + response.stage + '": ' + response.url + ' ' + JSON.stringify(response.headers));
    //};
    
    page.onResourceRequested = function (requestData, request) {
        if (requestData.method == 'POST'){
            console.log('method, url: ' + requestData.method + ', ' + requestData.url);
            console.log('Request ' + JSON.stringify(request, undefined, 4));
        }
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
