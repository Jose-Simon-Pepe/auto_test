Feature: Study Note Introducer
  Student's study notes Introducer.
  Component's aim is to take text study notes and let them usables.
  Notes has to be same format, and previously a supported format has to be choosen.

  Scenario: All right
    Given student has tagged non empty study notes
    And student has selected a note format
    When student introduces a study notes list
    Then system should enable student to make questions about

  Scenario: User tries to introduce notes without select format first
    Given student has no selected notes format
    When student introduces a study notes list
    Then system should not put note into
    And should notify user that he has to select notes format first

  Scenario: Study note has wrong at least one of its attributes
    Given study note lacks any of its attributes
    When student introduces a study notes list
    Then system should not put note into
    And system should tell user that attribute is missing 

  Scenario: Study note is not text file
    Given study note is not a text file
    When student introduces a study notes list
    Then system should not put note into
    And system should tell user that note is not text file
