from noteintroducer.agents.memory_supported_formats_storage import MemorySupportedFormat
from noteintroducer.agents.note_reader_config import NoteReaderConfig 
from cases.insert_note import select_format

#TODO: In select_expected_note_format se estaba usando 
# un tipo de dato diferente para obtener los formatos, por
# lo que ahora esta usando array. Probablemente serviria un dto
#TODO: Format should exist! make an enum

    

def test_insert_note_should_able_user_to_select_format():
    sup_for_store = MemorySupportedFormat()
    note_reader_conf = NoteReaderConfig()
    select_format(format="format1",
                  format_storage=sup_for_store,
                  note_reader_config= note_reader_conf)
    assert note_reader_conf._format['name'] == 'format1'
    assert note_reader_conf._format['title'] == '# '
    assert note_reader_conf._format['topic'] == '#'
