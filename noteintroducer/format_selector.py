class FormatSelector:
    def __init__(self,format_storage=None):
        self._load_supported_formats(format_storage=format_storage)

    def get_all_format(self):
        return self._supported_format

    def _load_supported_formats(self,format_storage=None):
        self._supported_format = format_storage.get_all()

