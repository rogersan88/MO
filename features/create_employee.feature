Feature: Create Employee

  @API
  Scenario: Verify POST call for single user
    When User sends "POST" call to endpoint "api/users"
      | Name   | Job  |
      | Test | Automation |
    Then User verifies the status code is "201"
    And User verifies POST response body contains following information
      | Name   | Job  |
      | Test | Automation |
