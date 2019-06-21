Feature: Testing the functionalities of Revolut website

   @verify_community_search @functional
   Scenario: Verify the search functionality of Revolut Community webpage
    Given the Revolut website home page is successfully opened
    When Community sub menu is selected from the Help menu
    Then it should be successfully navigated to the Community webpage
    When a topic titled We got a banking website is selected from the list of topics
    Then it should be successfully be navigated to the selected topic

   @verify_shortcuts @functional
   Scenario: Verify the Revolut Community webpage's shortcuts
    Given the Revolut website home page is successfully opened
    When Community sub menu is selected from the Help menu
    Then it should be successfully navigated to the Community webpage
    When a keyboard shortcut to go to TOP POSTS is pressed
    Then the TOP POSTS navigation bar must be selected
    When a keyboard shortcut to go to CATEGORIES is pressed
    Then the CATEGORIES navigation bar must be selected
    When a keyboard shortcut to go to LATEST POSTS is pressed
    Then the LATEST POSTS navigation bar must be selected
    When a keyboard shortcut to go to HAMBURGER MENU is pressed
    Then the HAMBURGER MENU screen must be displayed in the application
    When a keyboard shortcut to go to HELP is pressed
    Then the HELP screen must be displayed in the application
    When a keyboard shortcut to go to SEARCH BOX is pressed
    Then the SEARCH BOX must be displayed in the application

   @change_country_label   @functional
   Scenario: Verify the country change functionality of Revolut
    Given the Revolut website home page is successfully opened
    When United Kingdom country label is selected from the bottom left page
    Then change country webpage must be displayed
    When United States country is selected from the list of countries
    Then the url for the US revolut website must be opened
