from abc import ABC,abstractmethod
class NOTEREADERCONFIG(ABC):
    """Note Reader Config Protocol"""

    @abstractmethod
    def load_config(self):
        """Load note reader config"""

    @abstractmethod
    def set_expected_note_format(self,format=None):
        """Set expected study notes format"""
