import codecs
hexstring = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
decoded_message = codecs.decode(hexstring,'hex')
encoded_base64 = codecs.encode(decoded_message,'base64')

print (decoded_message.decode())
print(encoded_base64.decode())