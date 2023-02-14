Feature: Test the log in and sign up links functionality on jules.app

  Scenario: Check that the sign up link takes user to sign up page
    Given SignIn Page: That I am on the jules.app sign in page
    When SignIn Page: I click on the "Sign up" link
    Then SignUp Page: I am taken to the sign up page

  Scenario: Check that the log in link takes user to sign in page
    Given SignUp Page: I am on the jules.app sign up page
    When SignUp Page: I click on the "Log in" link
    Then SignUp Page: I am taken to the sign in page