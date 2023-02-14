Feature: Test the sign in feature of jules.app

  Scenario: Check that the user cannot attempt log in without entering a password
    Given SignIn Page: That I am on the jules.app sign in page
    When SignIn Page: I input a correct email
    And SignIn Page: I leave the password field empty
    Then SignIn Page: "Please enter your password!" error is displayed
    And SignIn Page: The log in button is disabled

