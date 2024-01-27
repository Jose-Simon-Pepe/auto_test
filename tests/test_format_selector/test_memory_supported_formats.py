from autoquiz.noteintroducer.agents.memory_supported_formats_storage import MemorySupportedFormat

def test_sut_should_get_all_supported_formats_from_memory():
    supported_formats = ['format1','format2']
    memory = list(supported_formats)
    sut = MemorySupportedFormat(storage=memory)
    assert sut.get_all(supported_formats)

def test_sut_should_get_supported_formats_by_name():
    format1 = {
        "name":"format1",
        "title":"# ",
        "topic" : "#",
        "body":"*"
    }
    format2 = {
        "name":"format2",
        "title":"= ",
        "topic" : "//=",
        "body":"*"
    }
    supported_formats = [format1,format2]
    memory = list(supported_formats)
    sut = MemorySupportedFormat(storage=memory)
    assert sut.get_by_name(name="format1") == supported_formats[0]

#NOTE: Integration test
def test_sut_should_get_a_default_values_set():
    all =  MemorySupportedFormat().get_all()
    assert all['format1']['title']=="# "

