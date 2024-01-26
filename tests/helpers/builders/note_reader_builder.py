from noteintroducer.note_reader import NoteReader
from noteintroducer.format_selector import FormatSelector

class NoteReaderBuilder:
    def __init__(self):
        self._note_reader_config =  NoteReaderConfig()
        self._format_selector = FormatSelectorFactory(note_reader_config=note_reader_config).format_selector
        self._format_expected = "format1"

    def set_format_selector(self,format_selector):
        self._format_selector = format_selector
        return self

    def set_format_expected(self,format_expected):
        self._format_expected = format_expected
        return self

    def build(self):
        self._format_selector.select_expected_note_format(expected=self._format_expected)
        return NoteReader(config=self._note_reader_config)
