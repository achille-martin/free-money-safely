#!/usr/bin/python3

# Required packages and tools
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging as log_tool
import datetime
import os

# Main function
def main():
    
    logger.debug('SimpleSearch::main - Entering function...')

    # Instantiate driver and browser
    logger.debug('SimpleSearch::main - Selenium driver being instantiated for Firefox browser')
    driver = webdriver.Firefox()
    logger.debug('SimpleSearch::main - Selenium driver instantiated for Firefox browser')

    # Open webpage in headfull mode
    target_webpage = "https://dev.to"
    logger.debug('SimpleSearch::main - Selenium trying to open webpage: ' + str(target_webpage))
    driver.get(target_webpage)
    logger.info('SimpleSearch::main - STEP 1 - Selenium opened webpage: ' + str(target_webpage))

    # Confirm desired page has been reached
    try:
        logger.debug('SimpleSearch::main - Selenium trying to confirm webpage is the desired one')
        assert "DEV" in driver.title
        logger.debug('SimpleSearch::main - Opened webpage confirmed to be the desired webpage')
    except Exception as e:
        raise Exception('The opened webpage might differ from the desired webpage: ' + str(target_webpage))

    # Look for search bar element
    logger.debug('SimpleSearch::main - Selenium looking for search bar')
    search_bar = driver.find_element(By.NAME, "q")
    logger.debug('SimpleSearch::main - Selenium found search bar:\n' + str(search_bar))

    # Input "hello" into the search bar
    sentence_to_search = "Hello"
    logger.debug('SimpleSearch::main - Selenium trying to input ' + str(sentence_to_search) + ' in search bar')
    search_bar.send_keys(sentence_to_search)
    logger.debug('SimpleSearch::main - Selenium input ' + str(sentence_to_search) + ' in search bar')

    # Start the search
    # Tip: Replace spaces by dots and include the tag name at the beginning
    logger.debug('SimpleSearch::main - Selenium trying to start a search for ' + str(sentence_to_search) + ' via search bar')
    search_button = driver.find_element(By.CSS_SELECTOR, "button.c-btn.c-btn--icon-alone.absolute.inset-px.left-auto.mt-0.py-0")
    logger.debug('SimpleSearch::main - Selenium found button to start search')
    search_button.click()
    logger.debug('SimpleSearch::main - Selenium clicked on search button:\n' + str(search_button))
    logger.info('SimpleSearch::main - STEP 2 - Selenium found results for sentence to search: ' + str(sentence_to_search))

    logger.debug('SimpleSearch::main - ...exiting function')

# Entry point
if __name__=="__main__":
    
    # Setup the logger
    HOME_DIR = os.path.expanduser( '~' )
    APP_DIR = HOME_DIR + '/Documents/free-money-safely'
    LOG_DIR = APP_DIR + '/log'
    os.mkdir(LOG_DIR)
    log_file_path = LOG_DIR + '/simple_search-{}.log'.format(datetime.datetime.strftime(datetime.datetime.now(), '%Y_%m_%d-%H_%M_%S'))
    logging_level = 'DEBUG'

    # Instantiate the logger
    logger = log_tool.getLogger(__name__)
    logger.setLevel(logging_level)
    file_handler = log_tool.FileHandler(log_file_path, mode='w+')
    formatter = log_tool.Formatter('[%(asctime)s][%(levelname)s] - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Call the main function
    logger.info('SimpleSearch::Entrypoint - Logger instantiated and set to ' + str(logging_level))
    main()

