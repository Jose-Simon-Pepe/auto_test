class StudyNoteReciever:
    def __init__(self):
        self._recieved:list

        
    def recieve_notes(self,notes:list=None):
        if type(notes) is not list:
            raise ValueError()
        for note in notes:
            if type(note) is not str:
                raise ValueError()
        self._recieved=notes
