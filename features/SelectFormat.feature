Feature: Select study note format
  User can select study note format according his owns notes.
  System has a limited set of supported formats.
  This is a sub-feature into Introduce Note

  Scenario: All right
    Given student has a list of all-same-formatted study notes
    And system displays a list of supported formats of signage characters
    When he sets existing signage characters format to be used
    Then system should use that to introduce new study notes

