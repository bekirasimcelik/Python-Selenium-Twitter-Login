# Twitter Login and NASA Visit

This project contains a code to login to twitter with python selenium and visit NASA account (This project has nothing to do with Nasa's account. I was just interested in Space and Science so I wanted to point you there :). You can test this code using unittest. Also, the code is broken into several python files for understandability.

## How does it work?

This project, using the selenium webdriver, goes to the twitter website, enters username and password, logs in, goes to the URL of the NASA account and displays the page. During these operations, name and xpath locator strategies are used to find web elements. It also defines web pages as classes with the Page Object Model (POM) design pattern.

## How to Install?

To run this project, follow these steps:

- Install Python 3.8 or higher on your computer.
- Install the Selenium library with the pip command: '!pip install selenium'
- Install the Chrome browser on your computer and download the appropriate version of chromedriver.
- In the directory where you downloaded your code, copy the chromedriver file to the main folder.
- Enter your username and password in the config.ini file. Attach this file to your .gitignore file and avoid sharing it on your github account.

## How to use it

To use this project, follow these steps:

- In the directory where you downloaded your code, navigate to the tests folder and run test_twitter.py: `python test_twitter.py`
- To see your code working, follow the chrome browser.
- To see the result of your code, check the console.

  ## Technologies Used

In this project, the following technologies were used:

- Python 3.8
- Selenium 3.141.0
- Chrome 96.0.4664.45
- Chromedriver 96.0.4664.45
- Unittest

## Addictions

For this project to work, the following dependencies are required:

- configparser 5.0.2
- urllib3 1.26.7

## Contributing

If you would like to contribute to this project, please follow these rules:

- If you want to add a new feature to the project or modify an existing feature, first open an issue and describe it in detail.
- Before writing your code, fork the current version of the project and create a new branch.
- When writing your code, write according to PEP 8 coding standards and add comment lines.
- After writing your code, test it using the unittest module and make sure there are no bugs.
- After pushing your code to your github account, send a pull request to the project and specify your issue number.
- Once your pull request is reviewed and approved, it will be merged into the project.
