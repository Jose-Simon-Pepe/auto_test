Feature: Study Note Reciever
  Student's study notes reciever.
  Component's aim is to take text study notes and let them usables

  Scenario: All right
    Given student has tagged non empty study notes
    When student put it into system
    Then system should enable student to make questions about

  Scenario: Study note has no tag
    Given study note has no tag
    When student put it into system
    Then system should not keep note in system
    And system should tell user that note has no identifiable tag

  Scenario: Study note has no content
    Given study note has no content
    When student put it into system
    Then system should not keep note in system
    And system should tell user that note has no content

  Scenario: Study note is not text
    Given study note is not a text file
    When student put it into system
    Then system should not keep note in system
    And system should tell user that note is not text file
