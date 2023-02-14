Feature: Test the sign in feature of Jules App

  Scenario: Check that the user cannot log in without entering password
    Given SignIn Page: That I am on yhe jules.app sign in page
    When SignIn Page: I input a correct email
    And SignIn Page: I leave the pass field empty
    Then SignIn Page: 'Please enter your password!" error is displayed
    And SignIn Page: The log in button is disabled

