from selenium import webdriver
from selenium.webdriver.common import action_chains, keys
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from time import sleep

# Save kepress combo to tuple for later use
keysTuple = (keys.Keys.ARROW_UP, keys.Keys.ARROW_RIGHT, keys.Keys.ARROW_DOWN,
                keys.Keys.ARROW_LEFT)

def play_game(website):
    # Create an instance of a Chrome session
    browser = webdriver.Chrome()
    browser.get(website)

    # Create an instance of an action chain
    actions = action_chains.ActionChains(browser)
    retryElem = browser.find_element_by_class_name("retry-button")
    while True:

        # Retry element always gets an exception, check page src before and
        # after keypress to know when game-over dialogue is present
        stopCheck = browser.page_source

        actions.send_keys(keysTuple).perform()

        stopCheck2 = browser.page_source


        # If no change to source we know we got game-over
        # Exceptions for the ODD time they occur

        if stopCheck == stopCheck2:
            # sleep to confirm the game-over dialogue is shown
            #sleep(4)
            try:
                retryElem.click()
            except NoSuchElementException:
                print("Passing No such element...")
                pass
            except ElementNotVisibleException:
                print("Passing element not visible..")
                pass

# Call the function with the target website
play_game('https://gabrielecirulli.github.io/2048/')
