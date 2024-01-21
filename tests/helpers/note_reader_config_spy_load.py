
class NoteReaderConfigSpy:
    def __init__(self):
        self._value = False

    def load_config(self):
        self._value = True


