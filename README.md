# DNV-GL Test Automation exercice
Test automation examples made in Selenium with Python

To be executed is necessary to install following tools:
- python
- pytest (with pip)
- allure-pytest (with pip)
- allure (with conda or similar)
- Selemnium (with pip)
- Selenium drivers (downloading chromedriver, geckodriver, etc)

# To Execute
First of all, you need to change myconfig.py in Framework directory to addapt to your needs.

Then, in order to execute, you need to use next sentences in DNVGL directory:
- py.test --alluredir=./results ./Source/Test/
- allure serve < DNVGL directory >\results
