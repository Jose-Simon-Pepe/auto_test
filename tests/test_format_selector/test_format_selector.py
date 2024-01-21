from noteintroducer.format_selector import FormatSelector 
from noteintroducer.protocols.supported_formats_storage import SUPPORTEDFORMATSSTORAGE
from noteintroducer.agents.memory_supported_formats_storage import MemorySupportedFormat

"""Format Selector Component"""
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
supported_formats= [format1,format2]

class FormatStorageStub(SUPPORTEDFORMATSSTORAGE):
    def __init__(self):
        self.format1 = {
            "name":"format1",
            "title":"# ",
            "topic" : "#",
            "body":"*"
        }
        self.format2 = {
            "name":"format2",
            "title":"= ",
            "topic" : "//=",
            "body":"*"
        }
        self.supported_formats = [self.format1,self.format2]
    def get_all(self):
        return self.supported_formats

    def get_by_name(self,name:str) -> dict:
        pass


format_storage_stub = FormatStorageStub()


def test_sut_should_get_all_supported_formats():
    sut = FormatSelector(format_storage=format_storage_stub)
    assert sut.get_all_format() == supported_formats
    

def test_sut_should_load_all_supported_formats_up_on_start():
    assert FormatSelector(format_storage_stub).get_all_format() is not None

#NOTE: Integration test
def test_sut_should_get_all_formats_from_memory_storage():
    supported_formats = ['format1','format2']
    memory_storage = MemorySupportedFormat(storage=supported_formats)
    sut = FormatSelector(format_storage=memory_storage)
    assert sut.get_all_format() == supported_formats

class NoteReaderConfigSpy:
    def __init__(self):
        self._expected = None

    def expected_note_format(self):
        return self._expected


    def set_expected_note_format(self,format=None):
        self._expected = format

def test_sut_should_allow_user_to_select_attribute_format():
    note_reader_config = NoteReaderConfigSpy()
    sut = FormatSelector(format_storage=format_storage_stub,
                         note_reader_config=note_reader_config)
    sut.select_expected_note_format(expected='format1')
    assert note_reader_config.expected_note_format()['format_expected']['name']=='format1'


    

