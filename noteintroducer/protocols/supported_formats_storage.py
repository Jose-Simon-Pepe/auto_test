from abc import ABC,abstractmethod
class SUPPORTEDFORMATSSTORAGE(ABC):
    @abstractmethod
    def get_all(self,storage=None):
        pass

