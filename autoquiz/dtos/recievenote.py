class RecieveNoteDTO:
    """Recieve note DTO: This's the DTO which deals with entry study notes to the system"""

    def __init__(self,content:str=None,tags:list=None):
        if (content,tags) is None:
            raise ValueError()
        self._content = content
        self._tags = tags

    def get_content(self):
        """Get note content"""
        return self._content

    def get_tags(self):
        """Get note tags or topics"""
        return self._tags
