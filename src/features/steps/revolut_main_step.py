from behave import given, when, then

from steps.constants import constants
from steps.locators.web_elements import COMMUNITY_SUB_MENU, HELP_MENU

@given('the Revolut website home page is successfully opened')
def verify_home_page(context):
    context.main_window = context.driver.current_window_handle
    assert context.reporter.verify_webpage_title(constants.HOME_PAGE_TITLE)

@when('Community sub menu is selected from the Help menu')
def navigate_to_community_menu(context):
    context.reporter.mouse_hover_on_element(HELP_MENU)
    context.reporter.check_element_and_click(COMMUNITY_SUB_MENU)

@then('it should be successfully navigated to the Community webpage')
def verify_community_page_navigation(context):
    context.reporter.switch_to_new_window_and_verify(1)
    context.community_window = context.driver.current_window_handle
    assert context.reporter.verify_webpage_title(constants.COMMUNITY_PAGE_TITE)
