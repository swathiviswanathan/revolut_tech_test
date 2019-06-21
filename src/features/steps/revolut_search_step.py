from behave import when, then

from steps.constants import constants

# pylint: disable=W0401
from steps.locators.web_elements import SEARCH_ICON, SEARCH_EDIT_FIELD, SEARCH_RESULT_FIRST

@when('a topic titled We got a banking website is selected from the list of topics')
def search_a_topic(context):
    context.reporter.check_element_and_click(SEARCH_ICON)
    context.reporter.check_element_and_send_keys(SEARCH_EDIT_FIELD, constants.SEARCH_TEXT)
    context.reporter.check_element_and_click(SEARCH_RESULT_FIRST)

@then('it should be successfully be navigated to the selected topic')
def verify_navigation_to_searched_topic(context):
    assert context.reporter.verify_webpage_title(constants.SEARCH_TEXT)