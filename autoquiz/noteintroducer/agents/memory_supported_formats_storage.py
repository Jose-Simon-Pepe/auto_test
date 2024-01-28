import tomllib
from autoquiz.noteintroducer.protocols.supported_formats_storage import SUPPORTEDFORMATSSTORAGE

class MemorySupportedFormat(SUPPORTEDFORMATSSTORAGE):
    """Supported Format storage following SUPPORTEDFORMATSTORAGE protocol"""

    def __init__(self,storage=None):
        if storage is None:
            self._storage = self._get_default(path="autoquiz/noteintroducer/data/default_formats.toml")
        else:
            self._storage = storage

    def get_all(self,storage=None):
        """Get all format supported"""
        return self._storage

    def get_by_name(self,name=None):
        """Get format supported by its name"""
        for storage in self._storage:
            if storage["name"]==name:
                return storage

    def _get_default(self,path:str=None):
        with open(path,'rb') as f:
            return tomllib.load(f)
