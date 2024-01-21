from noteintroducer.format_selector import FormatSelector
from noteintroducer.note_reader import NoteReader
from tests.helpers.format_selector_factory import FormatSelectorFactory
from tests.helpers.format_memory_factory import FormatMemoryFactory
from noteintroducer.agents.memory_supported_formats_storage import MemorySupportedFormat
from noteintroducer.protocols.note_reader_config import NOTEREADERCONFIG


memory_supported_format = FormatMemoryFactory().memory_supported_format 

class NoteReaderConfigSpy(NOTEREADERCONFIG):
    def __init__(self):
        self._value = False
        self._format = None

    def load_config(self):
        self._value =True
        return self._format

    def set_expected_note_format(self,format=None):
        self._format = format


def test_note_reader_should_load_config_at_start():
    spy_note_config = NoteReaderConfigSpy()
    sut = NoteReader(config=spy_note_config)
    assert spy_note_config._value


#NOTE: Integration test
#NOTE: Crear fichero de donde memory storage toma los tipos de formato admitidos
#NOTE: Lanzar excepcion en caso que el lector se use antes de configurar
def test_sut_should_read_expected_note_format():
    note_reader_config =  NoteReaderConfigSpy()
    format_storage = memory_supported_format
    format_selector = FormatSelectorFactory(note_reader_config=note_reader_config).format_selector
    format_selector.select_expected_note_format(expected='format1')
    sut = NoteReader(config=note_reader_config)
    assert sut.get_config()['format_expected']['name']=='format1'
