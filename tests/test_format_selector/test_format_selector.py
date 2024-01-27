from noteintroducer.format_selector import FormatSelector 
from tests.helpers.note_reader_config_spy import NoteReaderConfigSpy
from noteintroducer.protocols.supported_formats_storage import SUPPORTEDFORMATSSTORAGE
from noteintroducer.agents.memory_supported_formats_storage import MemorySupportedFormat
from tests.helpers.format_memory_factory import FormatMemoryFactory

"""Format Selector Component"""

format_storage_stub = FormatMemoryFactory().memory_supported_format



def test_sut_should_get_all_supported_formats():
    sut = FormatSelector(format_storage=format_storage_stub)
    assert sut.get_all_format() == format_storage_stub.get_all()
    

def test_sut_should_load_all_supported_formats_up_on_start():
    assert FormatSelector(format_storage_stub).get_all_format() is not None

#NOTE: Integration test
def test_sut_should_get_all_formats_from_memory_storage():
    memory_storage = FormatMemoryFactory().memory_supported_format
    sut = FormatSelector(format_storage=memory_storage)
    assert sut.get_all_format() == FormatMemoryFactory().memory_supported_format.get_all()


def test_sut_should_allow_user_to_select_attribute_format():
    note_reader_config = NoteReaderConfigSpy()
    sut = FormatSelector(format_storage=format_storage_stub,
                         note_reader_config=note_reader_config)
    sut.select_expected_note_format(expected='format1')
    assert note_reader_config.expected_note_format()['name']=='format1'

