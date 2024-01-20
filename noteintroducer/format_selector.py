class FormatSelector:
    def __init__(self,format_storage=None):
        self._format_storage= format_storage
        self._supported_format= ['format1','format2']

    def get_all_format(self):
        return self._supported_format

