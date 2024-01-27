from autoquiz.dtos.recievenote import RecieveNoteDTO
def test_dto_has_content_and_tags():
    sut = RecieveNoteDTO(content="content",
                         tags=['tag1','tag2'])
    sut_response_1 = sut.get_content()
    sut_response_2 = sut.get_tags()
    assert sut_response_1 == 'content'
    assert sut_response_2 == ['tag1','tag2']
