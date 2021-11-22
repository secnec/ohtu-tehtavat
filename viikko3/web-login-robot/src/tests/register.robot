*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Login Page

*** Test Cases ***
Register With Valid Username And Password
    Go To Register Page
    Set Username  kalle
    Set Password  kalle123
    Confirm Password  kalle123
    Click Button  Register
    Welcome Page Should be Open

Register With Too Short Username And Valid Password
    Go To Register Page
    Set Username  ka
    Set Password  kalle123
    Confirm Password  kalle123
    Click Button  Register
    Register Should Fail With Message  Minimum lenght of username is 3 characters.

Register With Valid Username And Too Short Password
    Go To Register Page
    Set Username  kalle
    Set Password  kalle12
    Confirm Password  kalle12
    Click Button  Register
    Register Should Fail With Message  Minimum lenght of password is 8 characters.

Register With Nonmatching Password And Password Confirmation
    Go To Register Page
    Set Username  kalle
    Set Password  kalle123
    Confirm Password  kalle122
    Click Button  Register
    Register Should Fail With Message  Passwords and password confirmation should match.

Login After Successful Registration
    Go To Register Page
    Set Username  kalle
    Set Password  kalle123
    Confirm Password  kalle123
    Click Button  Register
    Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Click Button  Login
    Title Should Be  Ohtu Application main page

Login After Failed Registration
    Go To Register Page
    Set Username  kalle
    Set Password  kalle123
    Confirm Password  kalle122
    Click Button  Register
    Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Click Button  Login
    Login Should Fail With Message  Invalid username or password