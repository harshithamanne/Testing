@file_upload
Feature: File upload validation

  Scenario Outline: Test for file upload <pass>
    When user goes to "https://platform.rescale.com" as "Login" page
    Then user sees "header" contains text "Sign in to Rescale"
    When user logs in
    Then user is on "https://platform.rescale.com/introduction/" as "Introduction" page
    When user clicks "files_link"
    Then user is on "https://platform.rescale.com/files/" as "Files" page
    And user sees "files_upload_label" contains text "<text>"
    When user uploads "<file>" in "file_upload"
    Then verify "<file_name>" is in uploaded file list

    Examples:
      | result | text                      | file     |   file_name   |
      | pass   | Upload from this computer | Test.txt |    Test.txt   |
