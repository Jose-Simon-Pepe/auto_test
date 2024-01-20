from noteintroducer.format_selector import FormatSelector
"""Format Selector Component"""



def test_sut_should_get_all_supported_formats():
    supported_formats = ['format1','format2']
    sut = FormatSelector()
    assert sut.get_all_format() == supported_formats
    
