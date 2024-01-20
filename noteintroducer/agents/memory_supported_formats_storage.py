from noteintroducer.protocols.supported_formats_storage import SUPPORTEDFORMATSSTORAGE

class MemorySupportedFormat(SUPPORTEDFORMATSSTORAGE):

    def __init__(self,storage=None):
        self._storage = storage

    def get_all(self,storage=None):
        return self._storage
