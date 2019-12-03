from utils import *
from packets import *
import six

DEFAULT_TRANSPORT_KEY = b'ZigBeeAlliance09'
packet = [
    0x61,0x88,0xe5,0x98,0xad,0x46,0x3f,0x00,0x00,0x08,0x00,0x46,0x3f,0x00,0x00,0x01,
    0x86,0x21,0x76,0x30,0x02,0x00,0x00,0x00,0x90,0x0b,0x04,0xff,0xff,0x2e,0x21,0x00,
    0x09,0x0f,0x1f,0x7c,0x6c,0xe3,0x9e,0x68,0x28,0x4f,0x58,0xc8,0x3e,0xd4,0xcf,0x0a,
    0x03,0xdb,0x2d,0xd8,0xe5,0xf7,0x38,0x89,0xb6,0xa5,0x4c,0x63,0xe3,0x6a,0x02,0xc7,
    0xcb,0x52,0x2d,0xf5,0xf8,0x89,0xf9,0x44,0x64
]
frame = Dot15d4FCS(packet)

if frame is not None and ZigbeeSecurityHeader in frame:
    extended_source_bytes = extended_address_bytes(get_extended_source(frame))
    decrypted, valid = zigbee_packet_decrypt(zigbee_trans_key(DEFAULT_TRANSPORT_KEY), frame, extended_source_bytes)
    decrypted = bytes(decrypted)
    if decrypted[0] == 0x05:
        print("Transport key detected")
        print(["0x{:02x}".format(x) for x in decrypted[2:18]])