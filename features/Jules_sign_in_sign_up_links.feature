Feature: Test the anchor links functionality on the jules.app sign in page

  Scenario: Check that the sign up link takes user to sign up page
    Given SignIn Page: That I am on the jules.app sign in page
    When SignIn Page: I click on the Sign Up link
    Then SignUp Page: I am taken to the Sign Up page
