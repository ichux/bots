import logging
import sys
import time
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(dotenv_path=str(BASE_DIR / '.env'))

CHROME = str(BASE_DIR / 'executes' / 'drivers' / 'chromedriver')
GECKODRIVER = str(BASE_DIR / 'executes' / 'drivers' / 'geckodriver')

QUICK_JAVA = str(BASE_DIR / 'executes' / 'quickjava-2.1.0-fx.xpi')

# print(BASE_DIR, Path(EXECUTABLE_PATH).parent)

LOGGER = logging.getLogger('bots')
LOGGER.setLevel(logging.DEBUG)

fh = logging.FileHandler(BASE_DIR / 'bot_logs.log')
fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

LOGGER.addHandler(fh)
LOGGER.addHandler(ch)


def flush_and_sleep(extent):
    sys.stdout.flush()
    time.sleep(extent)
