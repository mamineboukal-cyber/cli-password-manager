*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}         http://localhost:5000
${EMAIL}       amine@gmail.com
${PASSWORD}    Admin1234

*** Test Cases ***
Valid Login
    Open Browser    ${URL}    chrome    options=add_argument("--binary-location=C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe")
    Input Text      name:email      ${EMAIL}
    Input Text      name:password   ${PASSWORD}
    Click Button    Login
    Page Should Contain    Signed in successfully
    Close Browser