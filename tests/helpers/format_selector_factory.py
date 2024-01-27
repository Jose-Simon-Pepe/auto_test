from tests.helpers.format_memory_factory import FormatMemoryFactory
from autoquiz.noteintroducer.format_selector import FormatSelector
class FormatSelectorFactory:
    def __init__(self,note_reader_config=None):
        self._note_reader_config = note_reader_config
        self.format_selector = FormatSelector(format_storage=FormatMemoryFactory().memory_supported_format,
                                     note_reader_config=note_reader_config)
