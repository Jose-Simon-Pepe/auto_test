from noteintroducer.protocols.supported_formats_storage import NOTEREADERCONFIG

class NoteReaderConfig(NOTEREADERCONFIG):
    def __init__(self):
        self._format = None

    def load_config(self):
        return self._format

    def set_expected_note_format(self,format=None):
        self._format = format

