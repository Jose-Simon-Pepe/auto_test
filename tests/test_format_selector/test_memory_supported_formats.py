from noteintroducer.agents.memory_supported_formats_storage import MemorySupportedFormat

def test_sut_should_get_all_supported_formats_from_memory():
    supported_formats = ['format1','format2']
    memory = list(supported_formats)
    sut = MemorySupportedFormat(storage=memory)
    assert sut.get_all(supported_formats)
