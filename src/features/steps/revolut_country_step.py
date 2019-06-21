from behave import when, then

from steps.constants import constants
from steps.locators.web_elements import COUNTRY_LABEL, UNITED_STATES_REGION

@when('United Kingdom country label is selected from the bottom left page')
def select_country_label(context):
    context.reporter.check_element_and_click(COUNTRY_LABEL)

@then('change country webpage must be displayed')
def verify_country_navigation(context):
    assert context.reporter.verify_webpage_title(constants.CHANGE_COUNTRY_TITLE)

@when('United States country is selected from the list of countries')
def select_united_states(context):
    context.reporter.check_element_and_click(UNITED_STATES_REGION)

@then('the url for the US revolut website must be opened')
def verify_united_states_url(context):
    new_url = context.driver.current_url
    assert constants.US_URL_TEXT in new_url
