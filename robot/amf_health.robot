*** Settings ***
Library    RequestsLibrary

*** Variables ***
${AMF_URL}    http://localhost:8000

*** Test Cases ***
Verify AMF Health
    Create Session    amf    ${AMF_URL}
    ${resp}=    GET On Session    amf    /health
    Should Be Equal As Integers    ${resp.status_code}    200

