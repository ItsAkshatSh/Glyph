_URI_PREFIXES = (
    (b"http://www.", 0x01),
    (b"https://www.", 0x02),
    (b"http://", 0x03),
    (b"https://", 0x04),
)

def _abbreviate_uri(url):
    url_bytes = url.encode("utf-8")
    for prefix, code in _URI_PREFIXES:
        if url_bytes.startswith(prefix):
            return code, url_bytes[len(prefix):]
        return 0x00, url_bytes
    
def build_uri_record(url):
    identifier_code, uri_remainder = _abbreviate_uri(url)
    payload = bytes([identifier_code]) + uri_remainder
    
    header = 0xD1
    type_field = b"U"
    type_length = len(type_field)
    payload_length = len(payload)
    
    if payload_length > 255:
        raise ValueError("URI TOO LONG BUCKAROO")
    
    return bytes([header, type_length, payload_length]) + type_field + payload


def wrap_ndef_message(record_bytes):
    length = len(record_bytes)
    if length > 254:
        raise ValueError("NDEF message too long for single byte TLV length")
    
    return bytes([0x03, length]) + record_bytes + bytes([0xFE])

def build_url_ndef(url):
    return wrap_ndef_message(build_uri_record(url))