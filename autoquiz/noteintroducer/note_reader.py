class NoteReader:
    """Study Note Reader Domain Service"""

    def __init__(self,config=None):
        self._config = config.load_config()

    def get_config(self):
        """Get config to read notes"""
        return self._config

    def read_note(self,path:str=None) -> str:
        """Read study notes"""
        lines:list = None
        with open(path, mode='r',encoding='utf-8') as f:
            lines = f.readlines()
        return lines
