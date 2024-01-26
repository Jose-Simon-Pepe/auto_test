from noteintroducer.format_selector import FormatSelector
from noteintroducer.note_reader import NoteReader
from tests.helpers.format_selector_factory import FormatSelectorFactory
from tests.helpers.format_memory_factory import FormatMemoryFactory
from noteintroducer.agents.memory_supported_formats_storage import MemorySupportedFormat
from noteintroducer.protocols.note_reader_config import NOTEREADERCONFIG
from noteintroducer.agents.note_reader_config import NoteReaderConfig
from tests.helpers.note_reader_config_spy_load import NoteReaderConfigSpy
from os import path,remove
from tests.helpers.builders.note_reader_builder import NoteReaderBuilder
import pytest


memory_supported_format = FormatMemoryFactory().memory_supported_format 

@pytest.fixture(name="get_note")
def get_note():
    if path.isfile("tests/example_note"):
        remove("tests/example_note")
    note = open("tests/example_note",'w')
    note.write("content of note")
    note.close()



def test_note_reader_should_load_config_at_start():
    spy_note_config = NoteReaderConfigSpy()
    sut = NoteReader(config=spy_note_config)
    assert spy_note_config._value


#NOTE: Integration test
#NOTE: Lanzar excepcion en caso que el lector se use antes de configurar
def test_sut_should_read_expected_note_format():
    note_reader_config =  NoteReaderConfig()
    format_selector = FormatSelectorFactory(note_reader_config=note_reader_config).format_selector
    format_selector.select_expected_note_format(expected='format1')
    sut = NoteReader(config=note_reader_config)
    assert sut.get_config()['format_expected']['name']=='format1'

#NOTE: Integration
#NOTE: Create builder to agilise instantiation
def test_sut_should_read_a_doc(get_note):
    note_reader_config =  NoteReaderConfig()
    format_selector = FormatSelectorFactory(note_reader_config=note_reader_config).format_selector
    format_selector.select_expected_note_format(expected='format1')
    sut = NoteReader(config=note_reader_config)
    assert sut.read_note(path="tests/example_note")[0] == "content of note"


def test_sut_should_raise_if_doc_doesnt_contains_title_in_given_format():
    pass



