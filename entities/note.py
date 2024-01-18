class Note:
    def __init__(self,content:str=None):
        if content is None or content.rstrip()=="":
            raise VoidContentNoteException()
        self._content = content

class VoidContentNoteException(BaseException):
    pass
