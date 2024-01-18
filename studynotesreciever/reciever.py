from entities.note import Note 
from dtos.recievenote import RecieveNoteDTO

class StudyNoteReciever:
    def __init__(self):
        self._recieved:list

        
    def recieve_notes(self,notes:list=None):
        if type(notes) is not list:
            raise ValueError()
        for note in notes:
            if type(note) is not RecieveNoteDTO:
                raise NoNoteDTORecieved()
        self._recieved=notes
        to_return = list()
        for note in self._recieved:
            to_return.append(Note(content=note.get_content()))
        return to_return


class NoNoteDTORecieved(BaseException):
    pass
