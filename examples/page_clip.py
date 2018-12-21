import sys
import time

from selenium.common.exceptions import WebDriverException

from executes.browser import Driver

__author__ = "Chukwudi Nwachukwu"
__version__ = "1.0.0"


# noinspection PyProtectedMember
def get_data():
    """
    Aborts .css files and adverts linking to some pages
    :return:
    """
    # driver = Driver.phantomjs(image=True)
    # driver.command_executor._commands['executePhantomScript'] = ('POST', '/session/$sessionId/phantom/execute')
    #
    # script = """
    # var page = this;
    #
    # // being the actual size of the headless browser
    # // page.viewportSize = { width: 1440, height: 900 };
    #
    # var title = page.evaluate(function () {
    #     return document.title;
    # });
    #
    # var clipRect = page.evaluate(function(selector){
    #     // document.body.style.backgroundColor = "#000000";
    #     return document.querySelector(selector).getBoundingClientRect();
    # }, '#sponsors');
    #
    # // page.clipRect = {top: 0, left: 0, width: 200, height: 400};
    # page.clipRect = {
    #     top:    clipRect.top,
    #     left:   clipRect.left,
    #     width:  clipRect.width,
    #     height: clipRect.height
    # };
    #
    # output_file = new Date().getTime() + ".png"
    # page.render(output_file, {format: 'png'});  // page.render(new Date().getTime() + ".png");
    # """
    #
    # try:
    #     driver.get("https://pycon.ng")
    #     time.sleep(5)  # allows for proper load on some either slow network or resource intensive webpage
    #     driver.save_screenshot("pycon.png")  # save a snapshot
    #
    #     # check ghostdriver.log file for the result of the statement below
    #     driver.execute('executePhantomScript', {'script': script, 'args': []})
    # except WebDriverException, e:
    #     driver.save_screenshot("pycon-exception.png")
    #     print("WebDriverException: {} {}".format(e, sys.exc_info()[0]))
    # except (Exception,), e:
    #     print("Exception: {} {}".format(e, sys.exc_info()[0]))
    # finally:
    #     driver.quit()
    pass

if __name__ == '__main__':
    get_data()
