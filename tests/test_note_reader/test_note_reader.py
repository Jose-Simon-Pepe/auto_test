from noteintroducer.format_selector import FormatSelector
from noteintroducer.agents.memory_supported_formats_storage import MemorySupportedFormat
class NoteReaderConfigSpy:
    def __init__(self):
        self._value = False
        self._format = None

    def load_config(self):
        self._value =True
        return self._format

    def set_expected_note_format(self,format=None):
        self._format = format

class NoteReader:
    def __init__(self,config=None):
        self._config = config.load_config()

    def get_config(self):
        return self._config

def test_note_reader_should_load_config_at_start():
    spy_note_config = NoteReaderConfigSpy()
    sut = NoteReader(config=spy_note_config)
    assert spy_note_config._value

#NOTE: Integration test
#NOTE: Crear factory de format selector
#NOTE: Crear fichero de donde memory storage toma los tipos de formato admitidos
#NOTE: Crear memory factory
#NOTE: Lanzar excepcion en caso que el lector se use antes de configurar
#NOTE: revisar y corregir protocolo de memory supported format
def test_sut_should_read_expected_note_format():
    format1 = {
        "name":"format1",
        "title":"# ",
        "topic" : "#",
        "body":"*"
    }
    format2 = {
        "name":"format2",
        "title":"= ",
        "topic" : "//=",
        "body":"*"
    }
    note_reader_config =  NoteReaderConfigSpy()
    format_selector = FormatSelector(format_storage=MemorySupportedFormat(storage=[format1,format2]),
                                     note_reader_config=note_reader_config)
    format_selector.select_expected_note_format(expected='format1')
    sut = NoteReader(config=note_reader_config)
    assert sut.get_config()['format_expected']['name']=='format1'
