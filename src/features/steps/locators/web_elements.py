COUNTRY_LABEL = ".//*[contains(@class, 'CountryLabel_')]"
UNITED_STATES_REGION = ".//*[contains(text(), 'United States')]"

# CLOSE_APPLE_PAY = ".//*[@class='rvl-Icon-Icon rvl-Icon--color-gray rvl-Icon--size-xs']"
APPLE_PAY = ".//*[contains(text(), 'Apple Pay is here')]/../../div[@class='rvl-Banner-text-wrapper']"

HELP_MENU = ".//div[4]//span[contains(text(), 'Help')]"
COMMUNITY_SUB_MENU = ".//div[4]//a[contains(text(), 'Community')]"

SEARCH_ICON = ".//*[@id='search-button']"
SEARCH_EDIT_FIELD = ".//*[@id='search-term']"

SEARCH_RESULT = ".//*[@class='search-result-topic']"
SEARCH_RESULT_FIRST = ".//*[@class='search-result-topic']//li/a"

NAVIGATION_BAR = ".//*[@id='navigation-bar']"
SELECT_NAV_BAR = NAVIGATION_BAR+"/li/a[contains(text(), REPLACE_TEXT)]"
ACTIVE_NAV_BAR = NAVIGATION_BAR+"//a[@class='active']"

HAMBURGER_MENU = ".//*[@class='menu-panel drop-down']"
SHORTCUT_MENU = ".//*[@id='keyboard-shortcuts-help']"
MODAL_CLOSE = ".//div[@class='modal-close']/a"
