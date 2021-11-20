*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle2
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  x
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Fail With A Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  xKalle
    Set Password  x2
    Set Password Confirmation  x2
    Submit Credentials
    Register Should Fail With A Message  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  xKalle
    Set Password  kalle123
    Set Password Confirmation  kalle345
    Submit Credentials
    Register Should Fail With A Message  Password confirmation does not match

Login After Successful Registration
    Set Username  kalle2
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Go To Login Page
    Set Username  kalle2
    Set Password  kalle123
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  xKalle
    Set Password  x2
    Set Password Confirmation  password
    Submit Credentials
    Go To Login Page
    Set Username  xKalle
    Set Password  x2
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With A Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Credentials
    Click Button  Register

