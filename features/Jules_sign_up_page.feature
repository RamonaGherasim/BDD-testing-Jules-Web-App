Feature: Test the sign up feature of jules.app



  Scenario: Check that the user must use a valid email address to sign up
    Given SignUp Page: I am on the jules.app sign up page
    When SignUp Page: I select the "Personal" option
    When SignUp Page: I click continue
    When SignUp Page: I input correct first name and continue
    When SignUp Page: I input correct last name and continue
    When SignUp Page: I input an invalid email address
    Then SignUp Page: "Please enter a valid email address." error is displayed
    When SignUp Page: I clear the email input
    And SignUp Page: I input a valid email address
    Then SignUp Page: "Please enter a valid email address." error is no longer displayed
