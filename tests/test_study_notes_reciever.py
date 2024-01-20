from noteintroducer.reciever import StudyNoteReciever,NoNoteDTORecieved
from dtos.recievenote import RecieveNoteDTO
import pytest
from entities.note import Note

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

def test_sut_shouldnt_accept_list_with_nothing_but_reciever_note_dto():
    notes = [1,2,3,4]
    sut = StudyNoteReciever()
    with pytest.raises(NoNoteDTORecieved):
        sut.recieve_notes(notes)



#NOTE: Create builder or factory to create recievenotedto
#NOTE: Unitary test
def test_sut_should_return_notes_list():
    notes = [
        RecieveNoteDTO(content="dommie",
                            tags=['dommie']),
        RecieveNoteDTO(content="dommie2",
                            tags=['dommie2'])
             ]
    sut = StudyNoteReciever()
    sut_response = sut.recieve_notes(notes)
    assert len(sut_response) == 2
    assert type(sut_response[0]) == Note


def test_sut_should_return_notes_with_given_content_and_tags():
    notes = [
        RecieveNoteDTO(content="dommie",
                            tags=['dommie']),
        RecieveNoteDTO(content="dommie2",
                            tags=['dommie2'])
             ]
    sut = StudyNoteReciever()
    sut_response = sut.recieve_notes(notes)
    assert sut_response[0].get_content() == 'dommie'


