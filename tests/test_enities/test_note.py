import pytest
from entities.note import *


def test_note_should_has_a_content_not_null():
    content = ""
    with pytest.raises(VoidContentNoteException):
        Note(content=content)

def test_note_should_has_tags():
    sut = Note(content="Dommie",tags=['tag1','tag2'])
    sut_response = sut.get_tags()
    assert sut_response == ['tag1','tag2']
