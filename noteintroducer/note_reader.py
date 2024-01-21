
class NoteReader:
    def __init__(self,config=None):
        self._config = config.load_config()

    def get_config(self):
        return self._config
