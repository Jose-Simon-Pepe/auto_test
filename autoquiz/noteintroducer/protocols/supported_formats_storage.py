from abc import ABC,abstractmethod
class SUPPORTEDFORMATSSTORAGE(ABC):
    """Suported Formats Storage Protocol"""

    @abstractmethod
    def get_all(self,storage=None) -> list:
        """Get all autoquiz supported formats"""

    @abstractmethod
    def get_by_name(self,name:str=None) -> dict:
        """Get supported format by name"""
