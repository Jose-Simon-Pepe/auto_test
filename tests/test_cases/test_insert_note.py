from noteintroducer.agents.memory_supported_formats_storage import MemorySupportedFormat
from noteintroducer.agents.note_reader_config import NoteReaderConfig 
from cases.insert_note import select_format

#TODO: Format should exist! make an enum

    

def test_insert_note_should_able_user_to_select_format():
    sup_for_store = MemorySupportedFormat()
    note_reader_conf = NoteReaderConfig()
    select_format(format="format1",
                  format_storage=sup_for_store,
                  note_reader_config= note_reader_conf)
    assert note_reader_conf._format.get_name() == 'format1'
    assert note_reader_conf._format.get_title() == '# '
    assert note_reader_conf._format.get_topic() == '#'
