require 'rex/proto/rfb'

fixedkey = "\x17\x52\x6b\x06\x23\x4e\x58\x07"

STDOUT.write Rex::Proto::RFB::Cipher.decrypt ["D7A514D8C556AADE"].pack('H*'), fixedkey
