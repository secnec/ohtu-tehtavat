*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Input  new
    Input Credentials  kalle  kalle321
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123
    Output Should Contain  Minimum lenght of username is 3 characters.

Register With Valid Username And Too Short Password
    Input Credentials  kalle  kalle12
    Output Should Contain  Minimum lenght of password is 8 characters.

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  kallekalle
    Output Should Contain  Password should contain other characters, besides just letters.

*** Keywords ***
Input New Command
    Input  new