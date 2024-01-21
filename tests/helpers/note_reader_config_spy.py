class NoteReaderConfigSpy:
    def __init__(self):
        self._expected = None

    def expected_note_format(self):
        return self._expected


    def set_expected_note_format(self,format=None):
        self._expected = format
