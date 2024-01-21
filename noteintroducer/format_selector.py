class FormatSelector:
    def __init__(self,format_storage=None,
                 note_reader_config=None):
        self._note_reader_config = note_reader_config
        self._load_supported_formats(format_storage=format_storage)

    def get_all_format(self):
        return self._supported_format

    def _load_supported_formats(self,format_storage=None):
        self._supported_format = format_storage.get_all()

    def select_expected_note_format(self,expected:str=None):
        form_to_use = {'format_expected':None}
        for format in self._supported_format:
            if format['name']==expected:
                form_to_use['format_expected'] = format
        self._note_reader_config.set_expected_note_format(format=form_to_use)
