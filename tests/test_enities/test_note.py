import pytest
from entities.note import *

#NOTE: Note should has also taggs

def test_note_should_has_a_content_not_null():
    content = ""
    with pytest.raises(VoidContentNoteException):
        Note(content=content)
