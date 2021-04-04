# bots
A library to help you scrape the web with PhantomJS, Chrome or Firefox is an easy manner.

# explanation
A project that pulls Chrome, Gecko and PhantomJS codes for building a valid driver together. Please note that this
project was built on Mac OS but should work fine on other OS if the path issues are properly sorted. This project will
be continually altered, with your help till we all achieve the best library we can wish for.

## Setting Up the repo for development
This project uses `python3`.

## Reporting Issues
If you have found a bug or have a feature request, please report them at this repository issues section.

## Makefile
This file contains a help that you can read by just typing `make`

## Steps
1. Clone the repo
    ```git clone https://github.com/ichux/bots.git```

2. Create a virtual environment, activate it and *cd* into the cloned repository to run
    ```pip install -r requirements.txt```

3. Open [visits.txt](executes/visits.txt) and browse the links in it to download the necessary drivers. Once they are
    downloaded, put the executables in the *drivers* folder and name them whatever you want.

4. Whatever name you came up with in *step 3*, alter such in [executes-init](executes/__init__.py)
    For CHROME, for instance, mine is named __chromedriver__, etc


5. Believing that your virtual environment is activated and that you are in the cloned directory, running
    > python -m unittest discover normal_tests
   
    or
   
   > make normal_tests

   should output valid _variable_ messages like
    ```
    test_browsers.HeadlessBrowsers.test_body_save_buffer: 10.669
    .test_browsers.HeadlessBrowsers.test_bounding_rect: 6.522
    .test_browsers.HeadlessBrowsers.test_bounding_rect_save: 8.275
    .test_browsers.HeadlessBrowsers.test_js_call: 1.490
    .test_browsers.HeadlessBrowsers.test_time: 1.473
    ..
    ----------------------------------------------------------------------
    Ran 6 tests in 34.994s
    
    OK
    ```
