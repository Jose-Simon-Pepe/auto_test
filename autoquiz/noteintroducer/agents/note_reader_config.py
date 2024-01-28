from autoquiz.noteintroducer.protocols.note_reader_config import NOTEREADERCONFIG

class FormatExpected:
    """Format expected dto"""

    def __init__(self,name:str=None,
                 title:str=None,
                 topic:str=None):
        self._name = name
        self._title = title
        self._topic = topic

    def get_name(self) -> str:
        """Get format name"""
        return self._name

    def get_title(self) -> str:
        """Get format title spec"""
        return self._title

    def get_topic(self) -> str:
        """Get format topic spec"""
        return self._topic

class NoteReaderConfig(NOTEREADERCONFIG):
    """Note reader configuration module following NOTEREADERCONFIG protocol"""

    def __init__(self):
        self._format = None

    def load_config(self):
        """Load existing config"""
        return self._format

    def set_expected_note_format(self,format:FormatExpected=None):
        """Set a expected study note format"""
        self._format = format

class FormatExpectedBuilder:
    """Builder for improve code writing"""

    def __init__(self):
        self._name:str = None
        self._title:str = None
        self._topic:str = None

    def set_name(self,name):
        """Set Format name"""
        self._name = name
        return self

    def set_title(self,title):
        """Set title name"""
        self._title = title
        return self

    def set_topic(self,topic):
        """Set topic name"""
        self._topic = topic
        return self

    def build(self):
        """Build expected format"""
        return FormatExpected(name=self._name,
                              title=self._title,
                              topic=self._topic)
