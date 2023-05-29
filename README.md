# free-money-safely

## Purpose

This repo is intended to help people collect some free money in a safe and respectable way.

## Strategy

The technique used to collect free money relies on "free lotteries".

A "free lottery" is a lottery which is supported with advertising and lets people join "for free". It can be based on multiple varibles (for instance residential address) and consists in daily draws. Each participant of the daily draw must visit the website of the lottery to figure out whether they have won or not and they need to be the first amongst players at the same address (in the example) to claim the prize.

The challenge with "free lottery" is that it is:
* Time-consuming: need to check the results daily
* Luck-based: the winning draw can happen any date but it can't be predicted
* Competitive: multiple people might compete to get the same prize (and only the fastest gets it)

To solve these 3 problems, a robot server will be:
* Checking the results daily
* Reporting any winning draw to the user/master
* Claim the prize before everyone else if possible

## Implementation

### Technology

`Selenium` is a web scrapping and automation tool.
`Selenium` has been chosen over the simpler tool `beautifulsoup` because it can interact with the web page (press buttons, fill out forms).
Although `Selenium` is a bit more sensitive to UI changes, the assumption is that the "free lottery" websites don't vary much over time.

### Pre-requisites

1) Machine specifications

* Ubuntu 18.04
* Firefox 113.0.2 installed via `sudo apt-get install firefox`
* Python 3.6.9
* pip3 installed via `sudo apt install python3-pip`

```
export APP_DIR=~/Documents/free-money-safely
```

2) Virtual environment

```
cd $APP_DIR
pip3 install virtualenv
mkdir venv
cd venv
virtualenv free-money-safely-venv -p python3
source $APP_DIR/venv/free-money-safely-venv/bin/activate
```

3) Pip dependencies

```
cd $APP_DIR
pip3 install -r requirements.txt
```

4)  Firefox WebDriver

```
cd $APP_DIR
wget https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-linux64.tar.gz
tar -xzf geckodriver-v0.33.0-linux64.tar.gz
sudo rm geckodriver-v0.33.0-linux64.tar.gz
sudo mv geckodriver /usr/local/bin/
```

### Getting started

Run the following code to open Firefox and do a search:

```
python3 $APP_DIR/examples/simple_search.py
```

## Technicalities

Help pages can be found at: https://selenium-python.readthedocs.io/getting-started.html

### Locating elements

There are various ways to locate elements in a web page.
Right click on an element and inspect it.
See if you can spot any of the following:
* By ID (`id` will appear in the html code)
* By Name (`name` will appear in the html code)
* By XPath
* By Link Text (the first element with the link text matching the provided value will be returned - this only concerns text)
* By Tag Name (the first element with the given tag name will be returned - tags are identified by `<>`)
* By Class Name (`class` will appear in the html code)
* By CSS Selectors


