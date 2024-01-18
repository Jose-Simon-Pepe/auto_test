from entities.note import Note

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
        to_return = list()
        for note in self._recieved:
            to_return.append(Note(content=note))
        return to_return



