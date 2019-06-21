from behave import when, then
from selenium.webdriver.common.action_chains import ActionChains

from steps.constants import constants

# pylint: disable=W0401
from steps.locators.web_elements import MODAL_CLOSE, SHORTCUT_MENU, ACTIVE_NAV_BAR, HAMBURGER_MENU, SEARCH_EDIT_FIELD

@when('a keyboard shortcut to go to {shortcut} is pressed')
def press_keyboard_shortcut(context, shortcut):
    if "TOP" in shortcut:
        ActionChains(context.driver).send_keys(constants.SHORTCUT_TOP_POSTS).perform()

    elif "CATEGORIES" in shortcut:
        ActionChains(context.driver).send_keys(constants.SHORTCUT_CATEGORIES_POSTS).perform()

    elif "LATEST" in shortcut:
        ActionChains(context.driver).send_keys(constants.SHORTCUT_LATEST_POSTS).perform()

    elif "HAMBURGER" in shortcut:
        ActionChains(context.driver).send_keys(constants.SHORTCUT_HAMBURGER_MENU).perform()

    elif "SEARCH" in shortcut:
        ActionChains(context.driver).send_keys(constants.SHORTCUT_SEARCH_FIELD).perform()

    elif "HELP" in shortcut:
        ActionChains(context.driver).send_keys(constants.SHORTCUT_HELP).perform()

# A higher wait time is required here to achieve consistency
    context.reporter.additional_wait(10)

@then('the {shortcut} navigation bar must be selected')
@then('the {shortcut} must be displayed in the application')
def verify_shortcut_functionality(context, shortcut):
    if "TOP" in shortcut:
        assert "TOP" in (context.driver.find_element_by_xpath(ACTIVE_NAV_BAR).text).upper()

    elif "CATEGORIES" in shortcut:
        assert "CATEGORIES" in (context.driver.find_element_by_xpath(ACTIVE_NAV_BAR).text).upper()

    elif "LATEST" in shortcut:
        assert "LATEST" in (context.driver.find_element_by_xpath(ACTIVE_NAV_BAR).text).upper()

    elif "HAMBURGER" in shortcut:
        assert context.driver.find_element_by_xpath(HAMBURGER_MENU)

    elif "SEARCH" in shortcut:
        assert context.driver.find_element_by_xpath(SEARCH_EDIT_FIELD)

    elif "HELP" in shortcut:
        assert context.driver.find_element_by_xpath(SHORTCUT_MENU)
        context.reporter.check_element_and_click(MODAL_CLOSE)
