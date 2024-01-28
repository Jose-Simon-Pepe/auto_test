from autoquiz.noteintroducer.format_selector import FormatSelector

def select_format(format:str=None,
                  format_storage=None,
                  note_reader_config=None,
                  format_selector = None):
    """
    Use case 'select format'
    Needs: Format to set, Format storage, and Note Reader Config.
    It also acepts format selector for testing purposing
    """
    if format_selector is None:
        form_sel = FormatSelector(format_storage=format_storage,
                                  note_reader_config=note_reader_config)

    if None in [format,format_storage,note_reader_config]:
        raise ValueError()
    form_sel = FormatSelector(format_storage=format_storage,
                              note_reader_config=note_reader_config)
    form_sel.select_expected_note_format(format)

def display_list_of_supported_formats(format_storage_memory=None):
    """Use case 'display all supported formats'"""
    serv = FormatSelector(format_storage=format_storage_memory)
    return serv.get_all_format()
