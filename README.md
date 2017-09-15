# bots
A library to help you scrape the web with PhantomJS, Chrome or Firefox is an easy manner.

# explanation
A project that pulls Chrome, Gecko and PhantomJS codes for building a valid driver together. Please note that this
project was built on Mac OS but should work fine on other OS if the path issues are properly sorted. This project will
be continually altered, with your help till we all achieve the best library we can wish for.

## Setting Up the repo for development
This project uses `python2`. Please refer to [Py2orPy3](https://wiki.python.org/moin/Python2orPython3) for more 
detail

## executes/phantomlogs
Since phantomjs emits logs during usage, the logs, by default, get stored [phantomjs](executes/phantomlogs) You could 
also redirect it elsewhere.

## Reporting Issues
If you have found a bug or have a feature request, please report them at this repository issues section.

## Steps
1. Clone the repo
    ```git clone https://github.com/ichux/bots.git```

2. Create a virtual environment, activate it and *cd* into the cloned repository to run
    ```pip install -r requirements.txt```

3. Open [visits.txt](executes/visits.txt) and browse the links in it to download the necessary drivers. Once they are
    downloaded, put the executables in the *drivers* folder and name them whatever you want.

4. Whatever name you came up with in *step 3*, alter such in [executes-init](executes/__init__.py)
    For PhamtomJS, for instance, mine is named __phantomjs-2.1.1__, etc


5. Believing that your virtual environment is activated and that you are in the cloned directory, running
    ```python -m unittest discover tests/``` should output valid _variable_ messages like
    ```
    test_browsers.HeadlessBrowsers.test_chrome: 6.805
    .test_browsers.HeadlessBrowsers.test_firefox: 1.120
    .test_browsers.HeadlessBrowsers.test_phantom: 6.771
    ..
    ----------------------------------------------------------------------
    Ran 4 tests in 14.696s
    ```

6. You could also play around with the sample files found in [examples](examples) by typing, for example,
    ```python examples/abort_connections.py```