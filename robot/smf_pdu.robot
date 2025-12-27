*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${BASE_URL}    http://localhost:8001

*** Test Cases ***
Verify SMF PDU Session
    Create Session    smf    ${BASE_URL}
    ${payload}=    Create Dictionary    supi=imsi-00101    dnn=internet
    ${resp}=    POST On Session    smf    /pdu-session    json=${payload}
    Status Should Be    201
    Dictionary Should Contain Key    ${resp.json()}    status
    Should Be Equal    ${resp.json()["status"]}    ACTIVE

