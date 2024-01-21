class NoteReaderConfigSpy:
    def __init__(self):
        self._value = False

    def load_config(self):
        self._value =True

class NoteReader:
    def __init__(self,config=None):
        self._config = config.load_config()

def test_note_reader_should_load_config_at_start():
    spy_note_config = NoteReaderConfigSpy()
    sut = NoteReader(config=spy_note_config)
    assert spy_note_config._value
