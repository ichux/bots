import os

EXECUTABLE_PATH = os.path.realpath(os.path.dirname(os.path.realpath(__file__)))

PHANTOMJS = os.path.join(EXECUTABLE_PATH, 'drivers', 'phantomjs-2.1.1')
CHROME = os.path.join(EXECUTABLE_PATH, 'drivers', 'mac-chromedriver')
GECKODRIVER = os.path.join(EXECUTABLE_PATH, 'drivers', 'geckodriver')

QUICKJAVA = os.path.join(EXECUTABLE_PATH, 'quickjava-2.1.0-fx.xpi')
LOGIT = os.path.join(EXECUTABLE_PATH, 'phantomlogs')
