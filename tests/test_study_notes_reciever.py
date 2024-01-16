from studynotesreciever.reciever import StudyNoteReciever

def test_sut_should_recieve_notes():
    notes = list()
    sut = StudyNoteReciever()
    sut.recieve_notes(notes=notes)
    assert sut._recieved == notes



