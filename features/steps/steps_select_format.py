from cases.insert_note import select_format,display_list_of_supported_formats
from noteintroducer.agents.note_reader_config import NoteReaderConfig 
from noteintroducer.agents.memory_supported_formats_storage import MemorySupportedFormat

@given(u'user ask system to display a list of supported formats of signage characters')
def step_impl(context):
    context.note_reader_conf = NoteReaderConfig()
    context.format_storage = MemorySupportedFormat()
    display_list_of_supported_formats(format_storage_memory=context.format_storage)


@when(u'he sets existing signage characters format to be used')
def step_impl(context):
    select_format(format='format1',
                  format_storage=context.format_storage,
                  note_reader_config=context.note_reader_conf)


@then(u'system should use that to introduce new study notes')
def step_impl(context):
    assert context.note_reader_conf._format.get_name() == 'format1'
    assert context.note_reader_conf._format.get_title() == '# '
    assert context.note_reader_conf._format.get_topic() == '#'
