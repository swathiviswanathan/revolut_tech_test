# Revolut Technical Test

This BDD style automation framework is designed using python "behave".

## Sample report

![ezgif com-gif-maker-4](https://user-images.githubusercontent.com/32310710/59918290-31fa6780-941c-11e9-9f73-354dfa2e925f.gif)


## Installation

The required python libraries for framework execution are mentioned in `./requirements.txt` file. This is to provide easy dependency installation,

    pip3 install -r requirements.txt

It is advisible to create `virtualenv` in order to maintain independency.

*Note: the framework will work only on Python3 and above.*

### Drivers for web browsers

To execute scripts on browsers the execution machine should have the driver paths(chrome & firefox) set in system's environmental variables.

If driver paths are not set as part of environmental variable in your machine (you can confirm with `which chromedriver` & `which geckodriver`), please place the relevant drivers inside this repo and mention its "relative" path in `src/behave.ini` file for the framework to pick up appropriate drivers.

*Note: In mac `brew cask install chromedriver` & `brew install geckodriver` will install latest chromedriver version and will take care of setting the environmental variables*

### UserData in behave.ini

Attributes like `browser`, `url` are parameterised in order to achieve easy maintenance. These are placed in `src/behave.ini` file which can later be altered at runtime if required.

## Execution

*Note: Dry runs to ensure the test execution are performed only on chrome and firefox. Not tested in "safari" and it is ignored for now as its a technical test.*

Please ensure you are navigated into the `src` folder behave executing behave.

`behave` command must be used to trigger all the developed automation test scenario that is placed in `src/revolut_community.feature` file.

Parameters mentioned in `src/behave.ini` can be easily modified at run time like below,

    behave --tags=functional -D browser=chrome

## Reporting

It is easy and lean to use json result format as it will be lightweight and can later be used for html report generation and Jenkins integration. Use: `behave -f json -o ./results/result.json`.

### Allure

If required, "Allure" is another easy way to generate rich html reports locally. `allure-behave` python library is used for this purpose.

This currently supports taking snapshots on execution steps, which will be very useful in understanding the test execution and failures if any.

To setup, ensure `allure` is installed in your machine to view the reports,

On mac,

    brew install allure

and `allure-behave` python library is required.

    pip install allure-behave

Then, execute behave with allure formatted report,

    behave -f allure_behave.formatter:AllureFormatter -o results/allure

to view the generated report, use the below command with appropriate(relative) folder path.

    allure serve results/allure
