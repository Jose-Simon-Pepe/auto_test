from noteintroducer.agents.memory_supported_formats_storage import MemorySupportedFormat

class FormatMemoryFactory:
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
    memory_supported_format = MemorySupportedFormat(storage=[format1,format2])

