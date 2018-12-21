import os

EXECUTABLE_PATH = os.path.realpath(os.path.dirname(os.path.realpath(__file__)))

CHROME = os.path.join(EXECUTABLE_PATH, 'drivers', 'chromedriver')
GECKODRIVER = os.path.join(EXECUTABLE_PATH, 'drivers', 'geckodriver')

QUICKJAVA = os.path.join(EXECUTABLE_PATH, 'quickjava-2.1.0-fx.xpi')
