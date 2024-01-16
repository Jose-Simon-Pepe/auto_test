from studynotesreciever.reciever import StudyNoteReciever
import pytest

class StudyNote:
    pass

def test_sut_should_recieve_notes():
    notes = list()
    sut = StudyNoteReciever()
    sut.recieve_notes(notes=notes)
    assert sut._recieved == notes


def test_sut_shouldnt_accept_nothing_but_list():
    notes = ""
    sut = StudyNoteReciever()
    with pytest.raises(ValueError):
        sut.recieve_notes(notes)

def test_sut_shouldnt_accept_list_with_nothing_but_string():
    notes = [1,2,3,4]
    sut = StudyNoteReciever()
    with pytest.raises(ValueError):
        sut.recieve_notes(notes)


